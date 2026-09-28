import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

client = genai.Client(api_key=API_KEY)


def answer_question(question: str) -> str:
    if not question.strip():
        return "Please enter a question."

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=question
        )

        return response.text

    except Exception:
        return (
            "EduGenie Demo Answer\n\n"
            f"Your question: {question}\n\n"
            "Artificial Intelligence (AI) is a technology that enables "
            "computers to perform tasks that normally require human "
            "intelligence, such as learning, reasoning, problem-solving, "
            "and understanding language.\n\n"
            "Note: Gemini API is temporarily unavailable because the "
            "current free-tier quota has been reached."
        )