import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_resume_feedback(resume_text):
    """
    Uses GPT-4o to generate resume feedback for a given text input.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a career advisor who gives practical, structured resume suggestions."},
                {"role": "user", "content": f"Please review this resume and give constructive suggestions:\n\n{resume_text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error generating feedback: {str(e)}"
