from transformers import pipeline

print("Loading AI model... please wait")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

print("Model ready!\n")
symptoms = "I have frequent urination and extreme thirst"

diseases = [
    "Influenza",
    "Common Cold",
    "COVID-19",
    "Malaria",
    "Dengue Fever",
    "Diabetes",
    "Hypertension",
    "Pneumonia"
]

result = classifier(symptoms, candidate_labels=diseases)

print(f"Symptoms: {symptoms}\n")
print("--- RESULTS ---")
for disease, score in zip(result["labels"], result["scores"]):
    bar = "█" * int(score * 20)
    print(f"{disease:<20} {bar} {score*100:.1f}%")
