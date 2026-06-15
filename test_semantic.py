from src.semantic_analyzer import (
    calculate_topic_relevance
)

topic = "Artificial Intelligence"

essay = """
Artificial Intelligence is transforming
education and healthcare.
"""

score = calculate_topic_relevance(
    topic,
    essay
)

print(
    "Topic Relevance:",
    score
)