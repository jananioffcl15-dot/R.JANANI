import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

client = genai.Client(api_key=API_KEY)


def generate_quiz(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
Create a simple educational quiz about: {topic}

Give 5 multiple-choice questions.

For each question provide:
1. Question
A) Option
B) Option
C) Option
D) Option

Then provide:
Answer: [correct option]

Keep the questions suitable for students and easy to understand.
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text

    except Exception:
        return (
            "EduGenie Demo Quiz\n\n"
            f"Topic: {topic}\n\n"
            "1. What is the main purpose of learning this topic?\n"
            "A) To understand its basic concepts\n"
            "B) To avoid learning it\n"
            "C) To ignore examples\n"
            "D) None of these\n"
            "Answer: A\n\n"
            
            "2. Which approach helps students learn a new topic?\n"
            "A) Practice and revision\n"
            "B) Avoiding practice\n"
            "C) Skipping all examples\n"
            "D) Not reviewing mistakes\n"
            "Answer: A\n\n"
            
            "3. Why are examples useful when learning?\n"
            "A) They make concepts easier to understand\n"
            "B) They make learning impossible\n"
            "C) They remove the need for study\n"
            "D) They are unrelated to learning\n"
            "Answer: A\n\n"
            
            "4. What can improve understanding of a topic?\n"
            "A) Practice\n"
            "B) Confusion\n"
            "C) Avoiding questions\n"
            "D) Skipping revision\n"
            "Answer: A\n\n"
            
            "5. What is a good way to improve after a quiz?\n"
            "A) Review mistakes\n"
            "B) Ignore mistakes\n"
            "C) Stop studying\n"
            "D) Skip the topic\n"
            "Answer: A\n\n"
            
            "Note: Gemini API is temporarily unavailable because the "
            "current free-tier quota has been reached."
        )