import pandas as pd
from transformers import pipeline

print("Loading dataset...")
df = pd.read_csv("data/symptoms_dataset.csv")

print("Extracting diseases from dataset...")
diseases = sorted(df['Disease'].unique().tolist())
print(f"✅ Loaded {len(diseases)} diseases from dataset")

# Build disease → symptom lookup from dataset
symptom_columns = [f'Symptom_{i}' for i in range(1, 18)]
disease_symptoms = {}
for disease in diseases:
    rows = df[df['Disease'] == disease]
    symptoms_set = set()
    for col in symptom_columns:
        for val in rows[col].dropna():
            symptoms_set.add(val.strip().lower().replace('_', ' '))
    disease_symptoms[disease] = symptoms_set

all_known_symptoms = set()
for s in disease_symptoms.values():
    all_known_symptoms.update(s)

print("Loading AI model...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("✅ Model ready!\n")


def classify_symptoms(symptoms_text):
    text_lower = symptoms_text.lower()
    # Individual words from user input (ignore short words like "and", "the", "a")
    user_words = set(
        w for w in text_lower.replace(',', ' ').split()
        if len(w) > 3
    )

    # Step 1: Match user text against known symptoms in dataset
    matched = set()
    for symptom in all_known_symptoms:
        # Full phrase match: "skin rash" in "I have skin rash"
        if symptom in text_lower:
            matched.add(symptom)
        # Word-level match: "fever" matches "high fever", "body" matches "body ache"
        elif any(word in user_words for word in symptom.split() if len(word) > 3):
            matched.add(symptom)

    # Step 2: Score each disease by symptom overlap
    scores = {}
    for disease, known in disease_symptoms.items():
        if known:
            overlap = len(matched & known)
            scores[disease] = overlap / len(known)

    # Step 3: If dataset matching found results, use them
    top_score = max(scores.values()) if scores else 0
    if top_score > 0:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [(d, s) for d, s in sorted_scores[:3]]

    # Step 4: Fallback to AI zero-shot if no keyword match
    result = classifier(symptoms_text, candidate_labels=diseases)
    return list(zip(result["labels"][:3], result["scores"][:3]))


