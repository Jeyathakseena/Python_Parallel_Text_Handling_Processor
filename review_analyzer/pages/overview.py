import streamlit as st
import pandas as pd
import os

def show():

    st.header("📊 System Overview")

    if os.path.exists("data/analyzed_reviews.csv"):

        df = pd.read_csv("data/analyzed_reviews.csv")

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Total Reviews", len(df))

        col2.metric(
        "Positive",
        len(df[df["Sentiment"]=="Positive"])
        )

        col3.metric(
        "Negative",
        len(df[df["Sentiment"]=="Negative"])
        )

        col4.metric(
        "Neutral",
        len(df[df["Sentiment"]=="Neutral"])
        )

    else:
        st.info("No data available yet. Upload reviews first.")