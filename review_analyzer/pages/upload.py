import streamlit as st
import pandas as pd
from utils.file_loader import load_file

def show():

    st.header("Upload Review Files")

    uploaded_files = st.file_uploader(
        "Upload CSV / TXT / DOCX files",
        accept_multiple_files=True
    )

    if uploaded_files:

        all_reviews = []

        for file in uploaded_files:

            df = load_file(file)

            if df is not None:
                all_reviews.append(df)

        reviews = pd.concat(all_reviews)

        reviews.to_csv("data/reviews.csv", index=False)

        st.success("Files uploaded successfully!")

        st.metric("Total Reviews Uploaded", len(reviews))