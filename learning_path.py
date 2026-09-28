def get_learning_recommendations(topic: str) -> list[str]:
    if not topic.strip():
        return ["Please enter a topic."]

    return [
        f"Learn the basic concepts of {topic}.",
        f"Practice simple examples of {topic}.",
        f"Work on small exercises related to {topic}.",
        f"Review your mistakes and revise {topic}."
    ]