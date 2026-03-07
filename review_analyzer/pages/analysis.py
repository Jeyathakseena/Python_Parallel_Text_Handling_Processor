import streamlit as st
import pandas as pd
import os

from utils.sentiment_engine import analyze_dataframe


def show():

    st.header("⚙ Run Review Analysis")

    if not os.path.exists("data/reviews.csv"):
        st.warning("Upload files first.")
        return

    if st.button("Start Analysis"):

        df = pd.read_csv("data/reviews.csv")

        # automatically detect review column
        possible_cols = ["Review","review","reviews","text","comment","feedback"]

        review_col = None

        for col in df.columns:
             if col.lower() in [c.lower() for c in possible_cols]:
                  review_col = col
                  break

        if review_col is None:
             st.error("No review column found in dataset.")
             st.write("Columns found:", df.columns.tolist())
             return

        # standardize column name
        df.rename(columns={review_col: "Review"}, inplace=True)

        with st.spinner("Analyzing reviews..."):

            result_df = analyze_dataframe(df)

        os.makedirs("data", exist_ok=True)

        result_df.to_csv("data/analyzed_reviews.csv", index=False)

        st.success("✅ Analysis Completed!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Reviews", len(result_df))
        col2.metric("Positive", (result_df["Sentiment"] == "Positive").sum())
        col3.metric("Negative", (result_df["Sentiment"] == "Negative").sum())