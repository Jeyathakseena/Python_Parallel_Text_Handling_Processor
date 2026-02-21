import csv
import sqlite3
from datetime import datetime

sentiment_scores = {

    # Room
    "spacious": 2,
    "comfortable": 2,
    "small": -1,
    "uncomfortable": -2,

    # Service / Staff
    "friendly": 2,
    "helpful": 2,
    "rude": -2,
    "slow": -1,

    # Cleanliness
    "clean": 2,
    "dirty": -2,
    "hygienic": 2,

    # Food
    "delicious": 2,
    "tasty": 1,
    "bland": -1,

    # Location
    "great location": 2,
    "convenient": 2,
    "far": -1,

    # Experience
    "amazing": 2,
    "excellent": 2,
    "terrible": -2,
    "worst": -2,
    "disappointing": -2
}

try:
    with open("tripadvisor_hotel_reviews.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reviews = list(reader)
except FileNotFoundError:
    print("CSV file not found.")
    exit()
except Exception as e:
    print("Error reading file:", e)
    exit()

try:
    conn = sqlite3.connect("task3_sentiment.db")
    cursor = conn.cursor()
except sqlite3.Error as e:
    print("Database error:", e)
    exit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    score REAL,
    sentiment TEXT,
    timestamp TEXT
)
""")

for row in reviews[:100]:

    text = row["Review"].lower()
    score = 0

    for word, value in sentiment_scores.items():
        score += text.count(word) * value

    if score > 1:
        sentiment = "Satisfied"
    elif score < -1:
        sentiment = "Dissatisfied"
    else:
        sentiment = "Neutral"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO results (text, score, sentiment, timestamp) VALUES (?, ?, ?, ?)",
        (text, score, sentiment, timestamp)
    )

conn.commit()

cursor.execute("SELECT * FROM results LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()    