import streamlit as st
import pandas as pd
import os
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def show():

    st.header("📊 Analytics Dashboard")

    if not os.path.exists("data/analyzed_reviews.csv"):
        st.warning("⚠ No analyzed data found. Please run analysis first.")
        return

    df = pd.read_csv("data/analyzed_reviews.csv")

    # =============================
    # METRICS
    # =============================

    total_reviews = len(df)
    positive = len(df[df["Sentiment"] == "Positive"])
    negative = len(df[df["Sentiment"] == "Negative"])
    neutral = len(df[df["Sentiment"] == "Neutral"])

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Reviews", total_reviews)
    col2.metric("Positive", positive)
    col3.metric("Negative", negative)
    col4.metric("Neutral", neutral)

    st.divider()

    # =============================
    # SENTIMENT PIE CHART
    # =============================

    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment","Count"]

    pie = px.pie(
        sentiment_counts,
        values="Count",
        names="Sentiment",
        title="Sentiment Distribution",
        color="Sentiment",
        color_discrete_map={
            "Positive":"green",
            "Negative":"red",
            "Neutral":"gray"
        }
    )

    st.plotly_chart(pie,use_container_width=True)

    # =============================
    # SENTIMENT BAR CHART
    # =============================

    bar = px.bar(
        sentiment_counts,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        title="Review Sentiment Comparison"
    )

    st.plotly_chart(bar,use_container_width=True)

    # =============================
    # SCORE DISTRIBUTION
    # =============================

    hist = px.histogram(
        df,
        x="Score",
        nbins=20,
        title="Sentiment Score Distribution"
    )

    st.plotly_chart(hist,use_container_width=True)

    st.divider()

    # =============================
    # WORD CLOUD
    # =============================

    st.subheader("☁ Most Frequent Words")

    text = " ".join(df["Review"].astype(str))

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots()

    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")

    st.pyplot(fig)

    st.divider()

    # =============================
    # KEYWORD ANALYSIS
    # =============================

    st.subheader("🔎 Top Keywords")

    words = text.lower().split()

    common = Counter(words)

    top_positive = common.most_common(10)

    keyword_df = pd.DataFrame(
        top_positive,
        columns=["Keyword","Frequency"]
    )

    keyword_chart = px.bar(
        keyword_df,
        x="Keyword",
        y="Frequency",
        title="Top Keywords"
    )

    st.plotly_chart(keyword_chart,use_container_width=True)

    st.divider()

    # =============================
    # REVIEW LENGTH ANALYSIS
    # =============================

    st.subheader("✍ Review Length Analysis")

    df["Length"] = df["Review"].astype(str).apply(len)

    length_chart = px.histogram(
        df,
        x="Length",
        nbins=30,
        title="Review Length Distribution"
    )

    st.plotly_chart(length_chart,use_container_width=True)
