import streamlit as st
import pandas as pd
import os

def show():

    st.header("Review Records")

    if not os.path.exists("data/analyzed_reviews.csv"):
        st.warning("⚠ No analyzed data found. Please run analysis first.")
        return

    df = pd.read_csv("data/analyzed_reviews.csv")

    search = st.text_input("Search Reviews")

    if search:
        df = df[df["Review"].str.contains(search, case=False)]

    sentiment = st.selectbox(
        "Filter Sentiment",
        ["All","Positive","Negative","Neutral"]
    )

    if sentiment != "All":
        df = df[df["Sentiment"] == sentiment]

    st.dataframe(df)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "reviews.csv"
    )