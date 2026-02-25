import csv
import sqlite3
import time
from datetime import datetime

room_keywords = {
    "spacious": 2,
    "comfortable": 2,
    "small": -1,
    "uncomfortable": -2
}

service_keywords = {
    "friendly": 2,
    "helpful": 2,
    "rude": -2,
    "slow": -1
}

clean_keywords = {
    "clean": 2,
    "dirty": -2,
    "hygienic": 2
}

food_keywords = {
    "delicious": 2,
    "tasty": 1,
    "bland": -1
}

location_keywords = {
    "great location": 2,
    "convenient": 2,
    "far": -1
}

with open("tripadvisor_hotel_reviews.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    reviews = list(reader)

reviews = reviews * 50

conn = sqlite3.connect("performance_with_index.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS results")

cursor.execute("""
CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    total_score REAL,
    overall_sentiment TEXT,
    timestamp TEXT
)
""")

start_insert = time.time()

for row in reviews:
    text = row["Review"].lower()

    total_score = 0

    for word, value in room_keywords.items():
        total_score += text.count(word) * value

    for word, value in service_keywords.items():
        total_score += text.count(word) * value

    for word, value in clean_keywords.items():
        total_score += text.count(word) * value

    for word, value in food_keywords.items():
        total_score += text.count(word) * value

    for word, value in location_keywords.items():
        total_score += text.count(word) * value

    if total_score > 1:
        overall_sentiment = "Satisfied"
    elif total_score < -1:
        overall_sentiment = "Dissatisfied"
    else:
        overall_sentiment = "Neutral"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO results (text, total_score, overall_sentiment, timestamp)
    VALUES (?, ?, ?, ?)
    """, (text, total_score, overall_sentiment, timestamp))

conn.commit()
end_insert = time.time()

print("Insert Time (With Index):", end_insert - start_insert)

#Index

cursor.execute("CREATE INDEX idx_sentiment ON results(overall_sentiment)")
conn.commit()



start_query = time.time()

cursor.execute("SELECT * FROM results WHERE overall_sentiment = 'Dissatisfied'")
rows = cursor.fetchall()

end_query = time.time()

print("Query Time (With Index):", end_query - start_query)

conn.close()