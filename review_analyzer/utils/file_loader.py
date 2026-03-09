import pandas as pd
from docx import Document


def is_text_column(series):
    """
    Check if a column contains meaningful text instead of numbers.
    """
    sample = series.dropna().astype(str).head(20)

    text_count = 0

    for val in sample:
        if any(c.isalpha() for c in val):  # check if letters exist
            text_count += 1

    return text_count >= len(sample) * 0.5  # at least 50% text


def find_review_column(df):

    keywords = ["review", "comment", "feedback", "text", "message"]

    # Step 1: Prefer columns with review-related names
    for col in df.columns:
        if any(k in col.lower() for k in keywords):
            if is_text_column(df[col]):
                return col

    # Step 2: Otherwise choose the first valid text column
    for col in df.select_dtypes(include="object").columns:
        if is_text_column(df[col]):
            return col

    return None


def load_file(uploaded_file):

    filename = uploaded_file.name

    # CSV
    if filename.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

        col = find_review_column(df)

        if col is None:
            return None

        return pd.DataFrame({"review": df[col]})

    # Excel
    elif filename.endswith(".xlsx"):

        df = pd.read_excel(uploaded_file)

        col = find_review_column(df)

        if col is None:
            return None

        return pd.DataFrame({"review": df[col]})

    # TXT
    elif filename.endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")

        reviews = text.split("\n")

        return pd.DataFrame({"review": reviews})

    # DOCX
    elif filename.endswith(".docx"):

        doc = Document(uploaded_file)

        reviews = [p.text for p in doc.paragraphs if p.text.strip()]

        return pd.DataFrame({"review": reviews})

    return None