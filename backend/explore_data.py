import pandas as pd

print("Loading dataset...")
df = pd.read_csv("data/symptoms_dataset.csv")

print(f"\n📊 Total rows:     {len(df)}")
print(f"📊 Total columns:  {len(df.columns)}")

print(f"\n🦠 Unique diseases: {df['Disease'].nunique()}")
print("\n--- Disease List ---")
for disease in sorted(df['Disease'].unique()):
    print(f"  {disease}")

print("\n--- Sample Rows (first 3) ---")
print(df.head(3).to_string())