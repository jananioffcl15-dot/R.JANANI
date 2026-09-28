from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import (
    TextRequest,
    QAResponse,
    ExplanationResponse,
    QuizResponse,
    SummaryResponse,
    LearningPathResponse,
)

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    description="AI-powered educational assistant built with FastAPI and Google Gemini.",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


@app.post("/qa", response_model=QAResponse)
async def qa(payload: TextRequest):
    answer = answer_question(payload.text)
    return QAResponse(answer=answer)


@app.post("/explain", response_model=ExplanationResponse)
async def explain(payload: TextRequest):
    explanation = explain_concept(payload.text)
    return ExplanationResponse(explanation=explanation)


@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: TextRequest):
    questions = generate_quiz(payload.text)
    return QuizResponse(quiz=questions)


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(payload: TextRequest):
    summary = summarize_text(payload.text)
    return SummaryResponse(summary=summary)


@app.post(
    "/learn/recommendations",
    response_model=LearningPathResponse
)
async def recommendations(payload: TextRequest):
    recommendations = get_learning_recommendations(payload.text)
    return LearningPathResponse(
        recommendations=recommendations
    )