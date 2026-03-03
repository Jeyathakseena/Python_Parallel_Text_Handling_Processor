import streamlit as st
import sqlite3
from datetime import datetime


conn = sqlite3.connect("reviews.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    score REAL,
    sentiment TEXT,
    uploaded_at TEXT
)
""")
conn.commit()


st.title("Review Sentiment Analyzer")

menu = st.sidebar.selectbox(
    "Select Page",
    ["Upload Reviews", "Analyze Reviews"]
)

if menu == "Upload Reviews":

    st.header("Upload Text Files")

    uploaded_files = st.file_uploader(
        "Upload one or more .txt files",
        type=["txt"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            text = file.read().decode("utf-8").lower()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                INSERT INTO reviews (text, uploaded_at)
                VALUES (?, ?)
            """, (text, timestamp))

        conn.commit()
        st.success("All files uploaded and stored successfully!")


elif menu == "Analyze Reviews":

    st.header("Run Analysis")

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


    if st.button("Run Sentiment Analysis"):

        cursor.execute("SELECT id, text FROM reviews WHERE score IS NULL")
        rows = cursor.fetchall()

        if not rows:
            st.warning("No new reviews to analyze.")
        else:
            for row in rows:
                review_id = row[0]
                text = row[1]

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
                    sentiment = "Satisfied"
                elif total_score < -1:
                    sentiment = "Dissatisfied"
                else:
                    sentiment = "Neutral"

                
                cursor.execute("""
                    UPDATE reviews
                    SET score = ?, sentiment = ?
                    WHERE id = ?
                """, (total_score, sentiment, review_id))

            conn.commit()
            st.success("Sentiment analysis completed successfully!")


    cursor.execute("SELECT id, score, sentiment, uploaded_at FROM reviews")
    results = cursor.fetchall()

    if results:
        st.subheader("Stored Review Results")

        for row in results:
            st.write(f"Review ID: {row[0]}")
            st.write(f"Score: {row[1]}")
            st.write(f"Sentiment: {row[2]}")
            st.write(f"Uploaded At: {row[3]}")
            st.write("---")
    else:
        st.info("No reviews found in database.")