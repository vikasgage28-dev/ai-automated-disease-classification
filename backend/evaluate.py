# Accuracy benchmark: runs every case in data/eval_cases.csv through the pipeline
# Usage (from backend/):  python evaluate.py
from collections import defaultdict

import pandas as pd

from pipeline import classify_symptoms, disease_names


def normalize(name: str) -> str:
    # Dataset labels contain stray/double spaces (e.g. 'Diabetes ', 'Paroymsal  Positional')
    return ' '.join(name.split()).lower()


cases = pd.read_csv("data/eval_cases.csv")

known = {normalize(d) for d in disease_names}
unknown = sorted({d for d in cases['expected_disease'] if normalize(d) not in known})
if unknown:
    raise SystemExit(f"Unknown labels in eval_cases.csv: {unknown}")

top1_hits = 0
top3_hits = 0
failures = []
per_disease = defaultdict(lambda: [0, 0])  # disease -> [top1 hits, total]

for _, row in cases.iterrows():
    expected = normalize(row['expected_disease'])
    predictions = classify_symptoms(row['symptoms'])
    predicted = [normalize(d) for d, _, _ in predictions]

    per_disease[expected][1] += 1
    if predicted[0] == expected:
        top1_hits += 1
        per_disease[expected][0] += 1
    if expected in predicted:
        top3_hits += 1
    else:
        failures.append((row['symptoms'], expected, predictions))

total = len(cases)
print("=" * 70)
print(f"Cases          : {total}")
print(f"Top-1 accuracy : {top1_hits / total:.1%}  ({top1_hits}/{total})")
print(f"Top-3 accuracy : {top3_hits / total:.1%}  ({top3_hits}/{total})")
print("=" * 70)

print("\nDiseases with Top-1 misses:")
for disease, (hits, count) in sorted(per_disease.items(), key=lambda kv: kv[1][0] / kv[1][1]):
    if hits < count:
        print(f"  {disease:<45} {hits}/{count}")

print(f"\nCases where the correct disease is NOT in the Top-3 ({len(failures)}):")
for symptoms, expected, predictions in failures:
    got = ', '.join(f"{d.strip()} {c:.0%}" for d, c, _ in predictions)
    print(f"  - \"{symptoms}\"\n      expected: {expected}\n      got     : {got}")
