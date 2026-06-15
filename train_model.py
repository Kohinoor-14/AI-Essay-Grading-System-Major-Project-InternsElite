import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ----------------------------------
# Load Dataset
# ----------------------------------

df = pd.read_csv("data/essay_dataset.csv")

# ----------------------------------
# Features and Target
# ----------------------------------

X = df[
    [
        "word_count",
        "sentence_count",
        "vocabulary_score",
        "readability_score"
    ]
]

y = df["score"]

# ----------------------------------
# Train Test Split
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------
# Model Training
# ----------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------------
# Evaluation
# ----------------------------------

predictions = model.predict(X_test)

accuracy = r2_score(
    y_test,
    predictions
)

print("\nModel Training Complete")
print(f"R² Score: {accuracy:.4f}")

# ----------------------------------
# Save Model
# ----------------------------------

with open(
    "models/essay_model.pkl",
    "wb"
) as file:

    pickle.dump(
        model,
        file
    )

print(
    "\nModel saved successfully:"
)
print(
    "models/essay_model.pkl"
)