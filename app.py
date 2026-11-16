
import streamlit as st
from tools import analyze_resume_pdf

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Application heading
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get AI-powered feedback "
    "on your skills, experience and improvements."
)

st.divider()

# PDF upload section
st.subheader("Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF only)",
    type=["pdf"]
)

# Analyze button
if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Analyze Resume", type="primary"):

        try:

            with st.spinner(
                "Analyzing your resume with AI..."
            ):

                result = analyze_resume_pdf(uploaded_file)

            st.success("Analysis completed successfully!")

            st.divider()

            st.subheader("Your Resume Analysis")

            st.markdown(result)

            # Download analysis report
            st.download_button(
                label="Download Analysis Report",
                data=result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

        except Exception as e:

            st.error(f"Error: {e}")
