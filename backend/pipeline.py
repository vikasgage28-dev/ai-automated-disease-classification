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

# Plain-English equivalents for clinical / unclear dataset terms
SYMPTOM_SYNONYMS = {
    'polyuria': 'frequent urination',
    'burning micturition': 'painful burning urination',
    'continuous feel of urine': 'constant urge to urinate',
    'spotting urination': 'blood spots in urine',
    'dischromic patches': 'discoloured skin patches',
    'nodal skin eruptions': 'bumps on the skin',
    'altered sensorium': 'confusion and drowsiness',
    'weakness of one body side': 'one sided body weakness or paralysis',
    'breathlessness': 'shortness of breath',
    'mucoid sputum': 'coughing up mucus',
    'rusty sputum': 'rust coloured phlegm',
    'blood in sputum': 'coughing up blood',
    'acidity': 'acid reflux and heartburn',
    'indigestion': 'upset stomach',
    'passage of gases': 'passing gas and bloating',
    'visual disturbances': 'flashing or zigzag lights in vision',
    'depression': 'feeling low and sad',
    'toxic look (typhos)': 'looking very ill',
    'malaise': 'feeling unwell',
    'lethargy': 'lack of energy',
    'diarrhoea': 'loose stools',
    'yellowish skin': 'jaundice',
    'coma': 'unconscious or extremely drowsy',
    'stomach bleeding': 'vomiting blood',
    'distention of abdomen': 'swollen belly',
    'fluid overload': 'fluid retention',
    'history of alcohol consumption': 'heavy drinking',
    'extra marital contacts': 'unprotected sexual contact',
    'patches in throat': 'white patches in throat',
    'muscle wasting': 'losing muscle mass',
    'palpitations': 'heart pounding',
    'fast heart rate': 'racing heartbeat',
    'enlarged thyroid': 'swollen neck gland',
    'cold hands and feets': 'always feeling cold',
    'abnormal menstruation': 'irregular periods',
    'swollen extremeties': 'swollen hands and feet',
    'prominent veins on calf': 'bulging leg veins',
    'spinning movements': 'room spinning',
    'scurring': 'acne scars',
    'silver like dusting': 'silvery scaly skin',
    'small dents in nails': 'pitted nails',
    'yellow crust ooze': 'yellow crusty oozing sores',
    'red spots over body': 'red spotty rash',
    'swelled lymph nodes': 'swollen glands',
    'irregular sugar level': 'high blood sugar',
    'excessive hunger': 'always hungry',
    'obesity': 'overweight',
    'bloody stool': 'blood in stool',
    'congestion': 'blocked stuffy nose',
    'throat irritation': 'sore throat',
}

# Well-known symptoms missing from the dataset profiles
EXTRA_DISEASE_SYMPTOMS = {
    'Diabetes': ['excessive thirst'],
    'Jaundice': ['yellowing of eyes'],
    'Hypoglycemia': ['shakiness and trembling'],
    'Migraine': ['sensitivity to light'],
}

# Build disease → symptom text (human-readable sentence for each disease)
symptom_columns = [f'Symptom_{i}' for i in range(1, 18)]
disease_symptom_text = {}
for disease in diseases:
    rows = df[df['Disease'] == disease]
    symptoms = set()
    for col in symptom_columns:
        for val in rows[col].dropna():
            symptoms.add(' '.join(val.strip().lower().replace('_', ' ').split()))
    symptoms.update(EXTRA_DISEASE_SYMPTOMS.get(disease.strip(), []))
    # "polyuria (frequent urination), fatigue, ..."
    disease_symptom_text[disease] = ', '.join(
        f"{s} ({SYMPTOM_SYNONYMS[s]})" if s in SYMPTOM_SYNONYMS else s
        for s in sorted(symptoms)
    )

print("Loading AI semantic model (BioBERT - medical)...")
model = SentenceTransformer('pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb')
# Default is 100 tokens; enriched profiles are longer
model.max_seq_length = 256
print("✅ Semantic model ready!")

# Pre-compute disease embeddings at startup (done once, reused for every request)
print("Computing disease embeddings...")
disease_names = list(disease_symptom_text.keys())
disease_texts = [disease_symptom_text[d] for d in disease_names]
disease_embeddings = model.encode(disease_texts, convert_to_tensor=True)
print(f"✅ Embeddings ready for {len(disease_names)} diseases\n")


# Softmax temperature: lower = bigger gap between top matches
TEMPERATURE = 0.05


def classify_symptoms(symptoms_text: str):
    # Encode the user's input into a 768-dimensional meaning vector
    user_embedding = model.encode(symptoms_text, convert_to_tensor=True)

    # Compute cosine similarity between user input and every disease profile
    # cosine_similarity returns values from -1 to 1; higher = more similar
    similarities = util.cos_sim(user_embedding, disease_embeddings)[0]

    # Convert similarities into probabilities across all diseases (sum to 1)
    probabilities = (similarities / TEMPERATURE).softmax(dim=0)

    # Get top 3 matches
    top_indices = probabilities.argsort(descending=True)[:3].tolist()

    results = []
    for idx in top_indices:
        disease = disease_names[idx]
        confidence = round(float(probabilities[idx]), 4)
        similarity = round(float(similarities[idx]), 4)
        results.append((disease, confidence, similarity))

    return results


