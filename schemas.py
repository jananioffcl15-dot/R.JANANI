from pydantic import BaseModel
from typing import List


class TextRequest(BaseModel):
    text: str


class QAResponse(BaseModel):
    answer: str


class ExplanationResponse(BaseModel):
    explanation: str


class QuizResponse(BaseModel):
    quiz: str


class SummaryResponse(BaseModel):
    summary: str


class LearningPathResponse(BaseModel):
    recommendations: List[str]