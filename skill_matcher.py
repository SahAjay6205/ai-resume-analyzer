import json
resume = """
Python developer with experience in 
ml, sql, FastAPI and data analysis.
"""
job_description = """
We are looking for a Python developer with experience in machine learning, SQL, FastAPI, and data analysis. The ideal candidate will have a strong understanding of Python programming, as well as experience with various libraries and frameworks used in data science and web development. Responsibilities include developing and maintaining applications, collaborating with cross-functional teams, and contributing to the overall success of our projects."""

def calculate_similarity(resume, job_description):
    resume_skills = extract_skills(resume)  
    job_skills = extract_skills(job_description)

    matched = [skill for skill in job_skills if skill in resume_skills]

    unmatched = [skill for skill in job_skills if skill not in resume_skills]

    score = (len(matched)/len(job_skills) * 100 if job_skills else 0)

    return {
        "matched_skills": matched,
        "unmatched_skills": unmatched,
        "similarity_score": score
    }
SKILLS = [
    "python",
    "sql",
    "fastapi",
    "machine learning",
    "docker",
    "git",
    "pandas",
    "numpy"
]

def extract_skills(text):
    text = text.lower()
    skills = [skill for skill in SKILLS if skill in text]
    # Extract skills from the text using simple keyword matching
    return skills
result = calculate_similarity(resume, job_description)
print(json.dumps(result, indent = 4))