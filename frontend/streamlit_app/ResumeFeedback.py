import streamlit as st
import openai
import os

st.title("📝 Resume Feedback")

openai.api_key = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8", errors="ignore")
    with st.spinner("Analyzing your resume with GPT..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're a career advisor helping students improve their resumes."},
                {"role": "user", "content": f"Please review this resume and give suggestions:\n\n{resume_text}"}
            ]
        )
        st.success("Feedback generated below:")
        st.write(response['choices'][0]['message']['content'])
