import streamlit as st
import os

# Import the modular function from backend
from backend.openai_api.resume_feedback import generate_resume_feedback

st.set_page_config(page_title="Resume Feedback | TalentBridge", layout="centered")
st.title("📝 Resume Feedback (AI-powered)")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["txt", "pdf"])

if uploaded_file:
    file_text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("Resume Preview:")
    st.code(file_text[:1000])  # show first 1000 characters

    if st.button("Get AI Feedback"):
        with st.spinner("Analyzing your resume with GPT..."):
            feedback = generate_resume_feedback(file_text)
            st.success("✅ Here's your personalized feedback:")
            st.write(feedback)
