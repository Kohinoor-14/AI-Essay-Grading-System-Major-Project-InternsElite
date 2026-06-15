from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_plagiarism(
        current_essay,
        previous_essays):

    if not previous_essays:
        return 0

    documents = [current_essay] + previous_essays

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        documents
    )

    similarities = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )

    max_similarity = similarities.max()

    return round(
        max_similarity * 100,
        2
    )