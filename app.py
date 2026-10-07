def analyze_resume(resume_text: str):
    words = resume_text.split()

    return{"word_count": len(words),
           "status": "Resume received sucessfully."}

resume = """
Python developer with experience in 
ml, sql, FastAPI and data analysis.
"""

result = analyze_resume(resume)

print(result)