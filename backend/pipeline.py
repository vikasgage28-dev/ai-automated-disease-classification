import os
import pandas as pd

# Use a local cache folder inside the project to avoid Windows permission issues
os.environ['HF_HOME'] = os.path.join(os.path.dirname(__file__), 'models_cache')

from sentence_transformers import SentenceTransformer, util

print("Loading dataset...")
df = pd.read_csv("data/symptoms_dataset.csv")

print("Extracting diseases from dataset...")
diseases = sorted(df['Disease'].unique().tolist())
print(f"✅ Loaded {len(diseases)} diseases from dataset")

# Build disease → symptom text (human-readable sentence for each disease)
symptom_columns = [f'Symptom_{i}' for i in range(1, 18)]
disease_symptom_text = {}
for disease in diseases:
    rows = df[df['Disease'] == disease]
    symptoms = set()
    for col in symptom_columns:
        for val in rows[col].dropna():
            symptoms.add(val.strip().lower().replace('_', ' '))
    # Join all symptoms into a natural sentence: "fever, headache, body ache"
    disease_symptom_text[disease] = ', '.join(sorted(symptoms))

print("Loading AI semantic model (all-MiniLM-L6-v2)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Semantic model ready!")

# Pre-compute disease embeddings at startup (done once, reused for every request)
print("Computing disease embeddings...")
disease_names = list(disease_symptom_text.keys())
disease_texts = [disease_symptom_text[d] for d in disease_names]
disease_embeddings = model.encode(disease_texts, convert_to_tensor=True)
print(f"✅ Embeddings ready for {len(disease_names)} diseases\n")


def classify_symptoms(symptoms_text: str):
    # Encode the user's input into a 384-dimensional meaning vector
    user_embedding = model.encode(symptoms_text, convert_to_tensor=True)

    # Compute cosine similarity between user input and every disease profile
    # cosine_similarity returns values from -1 to 1; higher = more similar
    similarities = util.cos_sim(user_embedding, disease_embeddings)[0]

    # Get top 3 matches
    top_indices = similarities.argsort(descending=True)[:3].tolist()

    results = []
    for idx in top_indices:
        disease = disease_names[idx]
        score = float(similarities[idx])
        # Clamp score to [0, 1] for the UI confidence bar
        confidence = round(max(0.0, min(1.0, score)), 4)
        results.append((disease, confidence))

    return results


