import unittest
import pandas as pd
from backend.job_match_api.match_engine import recommend_jobs

class TestJobMatchEngine(unittest.TestCase):
    def setUp(self):
        self.sample_jobs = pd.DataFrame({
            'job_title': ['Data Analyst', 'Marketing Intern'],
            'requirements': ['Python, SQL, Excel', 'Social Media, SEO, Email'],
        })

    def test_recommendation_with_match(self):
        skills = ['Python', 'Excel']
        result = recommend_jobs(skills, self.sample_jobs, top_n=1)
        self.assertEqual(result.iloc[0]['job_title'], 'Data Analyst')

    def test_no_matches(self):
        skills = ['C++', 'Rust']
        result = recommend_jobs(skills, self.sample_jobs, top_n=1)
        self.assertEqual(result.iloc[0]['match_score'], 0)

if __name__ == "__main__":
    unittest.main()
