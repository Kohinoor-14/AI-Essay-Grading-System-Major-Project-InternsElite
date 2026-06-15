from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# ----------------------------------
# Load Model
# ----------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ----------------------------------
# Topic Relevance
# ----------------------------------

def calculate_topic_relevance(
        topic,
        essay_text
):

    topic_embedding = model.encode(
        topic,
        convert_to_tensor=True
    )

    essay_embedding = model.encode(
        essay_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        topic_embedding,
        essay_embedding
    )

    score = float(
        similarity[0][0]
    )

    score = max(
        0,
        min(
            100,
            score * 100
        )
    )

    return round(score, 2)