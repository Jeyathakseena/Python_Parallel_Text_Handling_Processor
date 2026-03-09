import pandas as pd
import re
from utils.keyword_lists import positive_keywords, negative_keywords


positive_pattern = r"\b(" + "|".join(positive_keywords) + r")\b"
negative_pattern = r"\b(" + "|".join(negative_keywords) + r")\b"


def analyze_dataframe(df):

    df["Review"] = df["Review"].astype(str).str.lower()

    # count positive words
    df["pos_count"] = df["Review"].str.count(positive_pattern)

    # count negative words
    df["neg_count"] = df["Review"].str.count(negative_pattern)

    # score
    df["Score"] = (df["pos_count"] * 2) - (df["neg_count"] * 2)

    # sentiment classification
    df["Sentiment"] = "Neutral"
    df.loc[df["Score"] >= 4, "Sentiment"] = "Positive"
    df.loc[df["Score"] <= -4, "Sentiment"] = "Negative"

    # status
    df["Status"] = "Neutral"
    df.loc[df["Sentiment"] == "Positive", "Status"] = "Good"
    df.loc[df["Sentiment"] == "Negative", "Status"] = "Bad"

    return df[["Review", "Score", "Status", "Sentiment"]]