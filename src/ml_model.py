import pickle
import pandas as pd

# ----------------------------------
# Load Trained Model
# ----------------------------------

with open(
    "models/essay_model.pkl",
    "rb"
) as file:

    model = pickle.load(file)

# ----------------------------------
# Predict Score
# ----------------------------------

def predict_score(
        word_count,
        sentence_count,
        vocabulary_score,
        readability_score
):

    data = pd.DataFrame(
        [[
            word_count,
            sentence_count,
            vocabulary_score,
            readability_score
        ]],
        columns=[
            "word_count",
            "sentence_count",
            "vocabulary_score",
            "readability_score"
        ]
    )

    prediction = model.predict(data)[0]

    return round(prediction, 2)