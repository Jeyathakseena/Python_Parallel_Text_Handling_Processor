import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


def sentiment_pie(df):

    counts = df["Sentiment"].value_counts()

    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Sentiment Distribution",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    return fig


def sentiment_bar(df):

    counts = df["Sentiment"].value_counts()

    fig = px.bar(
        x=counts.index,
        y=counts.values,
        color=counts.index,
        title="Sentiment Count"
    )

    return fig


def score_histogram(df):

    fig = px.histogram(
        df,
        x="Score",
        nbins=25,
        title="Score Distribution"
    )

    return fig


def keyword_bar(keyword_list, title):

    df = pd.DataFrame(keyword_list, columns=["keyword"])

    counts = df["keyword"].value_counts().head(10)

    fig = px.bar(
        x=counts.index,
        y=counts.values,
        title=title
    )

    return fig
