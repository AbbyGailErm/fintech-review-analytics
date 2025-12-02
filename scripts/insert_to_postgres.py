import pandas as pd
import psycopg2

# 1️⃣ Load CSV
df = pd.read_csv("data/processed/reviews_with_sentiment.csv")

# If review_id doesn't exist, create one
if 'review_id' not in df.columns:
    df['review_id'] = range(1, len(df) + 1)

# 2️⃣ Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",   # database you created
    user="abbygail",         # your macOS username
    password="",             # leave blank if no password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 3️⃣ Insert banks and get bank_ids
banks = df['bank'].unique()
bank_id_map = {}
for bank in banks:
    cur.execute("INSERT INTO banks (bank_name) VALUES (%s) RETURNING bank_id;", (bank,))
    bank_id = cur.fetchone()[0]
    bank_id_map[bank] = bank_id
conn.commit()

# 4️⃣ Insert reviews
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (
            review_id, bank_id, review_text, rating, review_date, 
            sentiment_label, sentiment_score, identified_themes
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
    """, (
        row['review_id'],
        bank_id_map[row['bank']],
        row['review'],                 # or row['review_text'] depending on your CSV
        row['rating'],
        row['date'],
        row['sentiment_label'],
        row['sentiment_score'],
        row.get('identified_themes', None)  # optional
    ))
conn.commit()

# 5️⃣ Close connection
cur.close()
conn.close()

print("✅ CSV data successfully inserted into PostgreSQL!")
