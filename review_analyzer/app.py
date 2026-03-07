import streamlit as st

st.set_page_config(
    page_title="Review Analysis System",
    page_icon="📊",
    layout="wide"
)

# -------- UI Styling -------- #

st.markdown("""
<style>

.main-title{
font-size:40px;
font-weight:700;
color:#4A55A2;
}

.section-box{
background:#f2f5ff;
padding:15px;
border-radius:10px;
margin-bottom:10px;
border-left:6px solid #4A55A2;
}

.sidebar .sidebar-content{
background-color:#f7f9ff;
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">📊 Review Analysis Dashboard</div>', unsafe_allow_html=True)

st.write("Advanced system for analyzing millions of reviews with rule-based sentiment scoring.")

# -------- Navigation Sections -------- #

section_descriptions = {

"Overview": "View system statistics, stored chunks, and overall performance metrics.",

"Upload Files": "Upload multiple text, csv, or doc files to begin processing and analysis.",

"Run Analysis": "Analyze uploaded reviews using regex scoring and keyword sentiment engine.",

"View Records": "Browse, search, filter and download all processed reviews.",

"Analytics": "Visualize sentiment distribution, keyword insights, and trend charts.",

"Email Report": "Generate a PDF report and send the analysis results via email.",

"Clear Data": "Permanently delete all stored reviews and analysis results."

}


# Sidebar Navigation

st.sidebar.title("Navigation")

section = st.sidebar.radio(
"Select Section",
list(section_descriptions.keys())
)

st.sidebar.markdown("---")
st.sidebar.write(section_descriptions[section])

# Load pages dynamically

if section == "Overview":
    from pages.overview import show
    show()

elif section == "Upload Files":
    from pages.upload import show
    show()

elif section == "Run Analysis":
    from pages.analysis import show
    show()

elif section == "View Records":
    from pages.records import show
    show()

elif section == "Analytics":
    from pages.analytics import show
    show()

elif section == "Email Report":
    from pages.email_report import show
    show()

elif section == "Clear Data":
    from pages.clear_data import show
    show()