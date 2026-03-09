import streamlit as st
import os

def show():

    st.header("Clear Stored Data")

    if st.button("Delete All Data"):

        if os.path.exists("data/reviews.csv"):
            os.remove("data/reviews.csv")

        if os.path.exists("data/analyzed_reviews.csv"):
            os.remove("data/analyzed_reviews.csv")

        st.success("All data deleted.")