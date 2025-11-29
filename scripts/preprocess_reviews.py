import pandas as pd

# Load raw CSV
df = pd.read_csv("data/raw/reviews_raw.csv")

# 1️⃣ Remove duplicates
df.drop_duplicates(subset=['review', 'rating', 'date', 'bank'], inplace=True)

# 2️⃣ Handle missing data (drop rows where critical info is missing)
df.dropna(subset=['review', 'rating', 'date', 'bank'], inplace=True)

# 3️⃣ Normalize date format
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# 4️⃣ Save cleaned CSV
df.to_csv("data/processed/reviews_clean.csv", index=False)

print(f"Preprocessing completed! {len(df)} reviews saved to data/processed/reviews_clean.csv")
