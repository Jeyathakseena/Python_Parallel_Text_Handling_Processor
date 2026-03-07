import streamlit as st
from utils.report_generator import generate_report
from utils.email_sender import send_email


def show():

    st.header("📧 Email Analytics Report")

    email = st.text_input("Enter Email Address")

    if st.button("Generate & Send Report"):

        report_path = generate_report()

        if report_path is None:
            st.error("⚠ Please run analysis first.")
            return

        send_email(email, report_path)

        st.success("✅ Report sent successfully!")