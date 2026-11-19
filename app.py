
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get AI-powered feedback "
    "on your skills, experience and improvements."
)

st.divider()

st.subheader("Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Analyze Resume", type="primary"):

        try:
            with st.spinner("Analyzing your resume with AI..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf"
                    )
                }

                response = requests.post(
                    API_URL,
                    files=files,
                    timeout=300
                )

            if response.status_code == 200:

                data = response.json()
                result = data["analysis"]

                st.success("Analysis completed successfully!")

                st.divider()
                st.subheader("Your Resume Analysis")
                st.markdown(result)

                st.download_button(
                    label="Download Analysis Report",
                    data=result,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )

            else:
                error_message = response.json().get(
                    "detail",
                    "Something went wrong."
                )
                st.error(f"API Error: {error_message}")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI. Start your backend server.")

        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again.")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

        except (KeyError, ValueError) as e:
            st.error(f"Invalid API response: {e}")
