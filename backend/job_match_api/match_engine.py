import pandas as pd

def recommend_jobs(user_skills, job_df, top_n=5):
    """
    Recommends jobs based on keyword overlap between user skills and job requirements.

    Args:
    - user_skills (list): Skills from user's profile or resume
    - job_df (DataFrame): A dataframe with 'job_title' and 'requirements' columns
    - top_n (int): Number of jobs to return

    Returns:
    - Filtered DataFrame with top N matches
    """
    job_df['match_score'] = job_df['requirements'].apply(
        lambda x: sum(skill.lower() in x.lower() for skill in user_skills)
    )
    return job_df.sort_values(by='match_score', ascending=False).head(top_n)
