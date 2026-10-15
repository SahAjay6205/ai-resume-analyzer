from fastapi import FastAPI
from skill_matcher import calculate_similarity
from pydantic import BaseModel

app = FastAPI(title = "AI Resume Analyzer")

class ResumeRequest(BaseModel):
    resume: str
    job_description: str

@app.get("/")
def home():
    return{"message": "AI resume analyzer is running"}


@app.post("/analyze")
def analyze_resume(request: ResumeRequest):
    result = calculate_similarity(request.resume, request.job_description)
    return result