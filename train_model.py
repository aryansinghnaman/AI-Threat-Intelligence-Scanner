import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

print("Loading dataset...")

# Load dataset
data = pd.read_csv("dataset.csv")

print("Dataset loaded successfully")
print("Total rows:", len(data))

# -----------------------------
# Detect column names
# -----------------------------

url_column = data.columns[0]
label_column = data.columns[1]

urls = data[url_column]
labels = data[label_column]

# -----------------------------
# Convert labels if needed
# -----------------------------

labels = labels.map({
    "bad":1,
    "good":0,
    "phishing":1,
    "legitimate":0,
    "malicious":1,
    "benign":0,
    1:1,
    0:0
})

# -----------------------------
# Train test split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    urls,
    labels,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# -----------------------------
# Convert URLs to numerical data
# -----------------------------

vectorizer = TfidfVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -----------------------------
# Train model
# -----------------------------

print("Training model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train_vec, y_train)

# -----------------------------
# Accuracy
# -----------------------------

accuracy = model.score(X_test_vec, y_test)

print("Model Accuracy:", accuracy)

# -----------------------------
# Save model
# -----------------------------

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")