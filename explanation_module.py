def explain_concept(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic."

    topic = topic.strip()

    return (
        "EduGenie Demo Explanation\n\n"
        f"Topic: {topic}\n\n"
        f"{topic} is an important concept that can be understood "
        "by learning its basic definition, key features, examples, "
        "and practical applications.\n\n"
        "Key Points:\n"
        f"1. Understand the basic meaning of {topic}.\n"
        f"2. Learn the important features of {topic}.\n"
        f"3. Study simple examples of {topic}.\n"
        f"4. Practice using {topic} in real situations.\n\n"
        "Note: Gemini API is temporarily unavailable because the "
        "current free-tier quota has been reached."
    )