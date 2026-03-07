import pandas as pd
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from fpdf import FPDF
from collections import Counter
import plotly.express as px


def generate_report():

    if not os.path.exists("data/analyzed_reviews.csv"):
        return None

    df = pd.read_csv("data/analyzed_reviews.csv")

    

    os.makedirs("reports", exist_ok=True)

    # -------------------------
    # METRICS
    # -------------------------
    total = len(df)
    positive = len(df[df["Sentiment"] == "Positive"])
    negative = len(df[df["Sentiment"] == "Negative"])
    neutral = len(df[df["Sentiment"] == "Neutral"])
    avg_score = round(df["Score"].mean(), 2)

    # -------------------------
    # PIE CHART
    # -------------------------
    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]

    pie = px.pie(
        sentiment_counts,
        values="Count",
        names="Sentiment",
        color="Sentiment",
        color_discrete_map={
            "Positive": "green",
            "Negative": "red",
            "Neutral": "gray"
        },
        title="Sentiment Distribution"
    )

    pie_path = "reports/pie_chart.png"
    pie.write_image(pie_path)

    # -------------------------
    # BAR CHART
    # -------------------------
    bar = px.bar(
        sentiment_counts,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        title="Sentiment Comparison"
    )

    bar_path = "reports/bar_chart.png"
    bar.write_image(bar_path)

    # -------------------------
    # SCORE HISTOGRAM
    # -------------------------
    hist = px.histogram(
        df,
        x="Score",
        nbins=20,
        title="Score Distribution"
    )

    hist_path = "reports/histogram.png"
    hist.write_image(hist_path)

    # -------------------------
    # WORD CLOUD
    # -------------------------
    text = " ".join(df["Review"].astype(str))

    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    wc_path = "reports/wordcloud.png"

    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(wc_path)
    plt.close()

    # -------------------------
    # TOP KEYWORDS
    # -------------------------
    words = text.lower().split()
    common_words = Counter(words).most_common(10)

    keyword_df = pd.DataFrame(common_words, columns=["Keyword", "Frequency"])

    keyword_chart = px.bar(
        keyword_df,
        x="Keyword",
        y="Frequency",
        title="Top Keywords"
    )

    keyword_path = "reports/keywords.png"
    keyword_chart.write_image(keyword_path)

    # -------------------------
    # CREATE PDF
    # -------------------------

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "Review Analytics Report", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Total Reviews: {total}", ln=True)
    pdf.cell(0, 10, f"Positive Reviews: {positive}", ln=True)
    pdf.cell(0, 10, f"Negative Reviews: {negative}", ln=True)
    pdf.cell(0, 10, f"Neutral Reviews: {neutral}", ln=True)
    pdf.cell(0, 10, f"Average Score: {avg_score}", ln=True)

    pdf.ln(10)

    # Charts

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Sentiment Distribution", ln=True)

    pdf.image(pie_path, w=170)

    pdf.add_page()

    pdf.cell(0,10,"Sentiment Comparison",ln=True)
    pdf.image(bar_path, w=170)

    pdf.ln(10)

    pdf.cell(0,10,"Score Distribution",ln=True)
    pdf.image(hist_path, w=170)

    pdf.add_page()

    pdf.cell(0,10,"Word Cloud",ln=True)
    pdf.image(wc_path, w=170)

    pdf.ln(10)

    pdf.cell(0,10,"Top Keywords",ln=True)
    pdf.image(keyword_path, w=170)

    # Sample reviews

    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Sample Reviews", ln=True)

    pdf.set_font("Arial", "", 10)

    for i, row in df.head(10).iterrows():

        review = str(row["Review"])[:200]

        pdf.multi_cell(
            0,
            8,
            f"{row['Sentiment']} ({row['Score']}): {review}"
        )

    report_path = "reports/review_report.pdf"

    pdf.output(report_path)

    return report_path