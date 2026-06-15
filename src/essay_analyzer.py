from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob

from src.ml_model import predict_score
from src.semantic_analyzer import calculate_topic_relevance
from src.plagiarism import calculate_plagiarism


def analyze_essay(
        text,
        topic,
        previous_essays=None):

    if previous_essays is None:
        previous_essays = []

    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    clean_words = [
        word.lower()
        for word in words
        if word.isalpha()
    ]

    word_count = len(clean_words)

    sentence_count = len(sentences)

    unique_words = len(set(clean_words))

    # ----------------------------------
    # Vocabulary Score
    # ----------------------------------

    if word_count > 0:
        vocabulary_score = (
            unique_words / word_count
        ) * 100
    else:
        vocabulary_score = 0

    # ----------------------------------
    # Grammar Score
    # ----------------------------------

    blob = TextBlob(text)

    corrected = str(
        blob.correct()
    )

    grammar_errors = abs(
        len(corrected.split()) -
        len(text.split())
    )

    grammar_score = max(
        0,
        100 - grammar_errors * 2
    )

    # ----------------------------------
    # Readability Score
    # ----------------------------------

    avg_sentence_length = (
        word_count / sentence_count
        if sentence_count > 0
        else 0
    )

    readability_score = max(
        0,
        100 - abs(
            avg_sentence_length - 15
        ) * 2
    )

    # ----------------------------------
    # ML Score
    # ----------------------------------

    ml_score = predict_score(
        word_count,
        sentence_count,
        vocabulary_score,
        readability_score
    )

    # ----------------------------------
    # Topic Relevance
    # ----------------------------------

    topic_score = calculate_topic_relevance(
        topic,
        text
    )

    # ----------------------------------
    # Plagiarism Detection
    # ----------------------------------

    plagiarism_score = calculate_plagiarism(
        text,
        previous_essays
    )

    # ----------------------------------
    # Final Composite Score
    # ----------------------------------

    final_score = (
        grammar_score * 0.20 +
        vocabulary_score * 0.20 +
        readability_score * 0.15 +
        ml_score * 0.25 +
        topic_score * 0.15 +
        (100 - plagiarism_score) * 0.05
    )

    feedback = []

    if grammar_score < 70:
        feedback.append(
            "Improve grammar and sentence structure."
        )

    if vocabulary_score < 40:
        feedback.append(
            "Use more diverse vocabulary."
        )

    if readability_score < 70:
        feedback.append(
            "Improve sentence readability."
        )

    if topic_score < 50:
        feedback.append(
            "Essay is weakly related to the topic."
        )

    if plagiarism_score > 50:
        feedback.append(
            "High similarity detected with previous submissions."
        )

    if len(feedback) == 0:
        feedback.append(
            "Excellent essay quality."
        )

    return {

        "word_count": word_count,

        "sentence_count": sentence_count,

        "grammar_score": round(
            grammar_score,
            2
        ),

        "vocabulary_score": round(
            vocabulary_score,
            2
        ),

        "readability_score": round(
            readability_score,
            2
        ),

        "ml_score": round(
            ml_score,
            2
        ),

        "topic_score": round(
            topic_score,
            2
        ),

        "plagiarism_score": round(
            plagiarism_score,
            2
        ),

        "overall_score": round(
            final_score,
            2
        ),

        "feedback": feedback
    }