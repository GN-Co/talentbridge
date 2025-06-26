import unittest
from unittest.mock import patch
from backend.openai_api.resume_feedback import generate_resume_feedback

class TestResumeFeedback(unittest.TestCase):
    @patch('backend.openai_api.resume_feedback.openai.ChatCompletion.create')
    def test_generate_feedback_success(self, mock_openai):
        mock_openai.return_value = {
            'choices': [{'message': {'content': 'Your resume looks great!'}}]
        }

        result = generate_resume_feedback("Sample resume text here")
        self.assertIn("resume looks great", result.lower())

    @patch('backend.openai_api.resume_feedback.openai.ChatCompletion.create', side_effect=Exception("API error"))
    def test_generate_feedback_failure(self, mock_openai):
        result = generate_resume_feedback("This will fail")
        self.assertIn("error generating feedback", result.lower())

if __name__ == "__main__":
    unittest.main()
