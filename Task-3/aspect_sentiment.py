import csv
import sqlite3
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

try:
    with open("tripadvisor_hotel_reviews.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reviews = list(reader)
except FileNotFoundError:
    print("CSV file not found.")
    exit()

conn = sqlite3.connect("aspect_sentiment.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    room_status TEXT,
    service_status TEXT,
    clean_status TEXT,
    food_status TEXT,
    location_status TEXT,
    total_score REAL,
    overall_sentiment TEXT,
    timestamp TEXT
)
""")

for row in reviews[:500]:

    text = row["Review"].lower()

    room_score = 0
    service_score = 0
    clean_score = 0
    food_score = 0
    location_score = 0
    for word, value in room_keywords.items():
        room_score += text.count(word) * value

    for word, value in service_keywords.items():
        service_score += text.count(word) * value

    for word, value in clean_keywords.items():
        clean_score += text.count(word) * value

    for word, value in food_keywords.items():
        food_score += text.count(word) * value

    for word, value in location_keywords.items():
        location_score += text.count(word) * value

    room_status = "Yes" if room_score > 0 else "No"
    service_status = "Yes" if service_score > 0 else "No"
    clean_status = "Yes" if clean_score > 0 else "No"
    food_status = "Yes" if food_score > 0 else "No"
    location_status = "Yes" if location_score > 0 else "No"

    total_score = room_score + service_score + clean_score + food_score + location_score

    if total_score > 1:
        overall_sentiment = "Satisfied"
    elif total_score < -1:
        overall_sentiment = "Dissatisfied"
    else:
        overall_sentiment = "Neutral"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO results 
    (text, room_status, service_status, clean_status, food_status, location_status, total_score, overall_sentiment, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    (text, room_status, service_status, clean_status, food_status, location_status, total_score, overall_sentiment, timestamp))

    cursor.execute("SELECT * FROM results LIMIT 5")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

conn.commit()
conn.close()

