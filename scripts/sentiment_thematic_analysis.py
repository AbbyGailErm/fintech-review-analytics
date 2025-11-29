# scripts/sentiment_thematic_analysis.py

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -------------------------
# 1. Load cleaned reviews
# -------------------------
df = pd.read_csv("data/processed/reviews_clean.csv")

# -------------------------
# 2. Sentiment Analysis
# -------------------------
sia = SentimentIntensityAnalyzer()

# Compute sentiment score and label
df['sentiment_score'] = df['review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(
    lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
)

# Save interim CSV with sentiment
df.to_csv("data/processed/reviews_with_sentiment.csv", index=False)

# -------------------------
# 3. Thematic / Keyword Extraction
# -------------------------
themes_per_bank = {}

for bank in df['bank'].unique():
    bank_reviews = df[df['bank'] == bank]['review'].astype(str)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=20)
    X = vectorizer.fit_transform(bank_reviews)
    keywords = vectorizer.get_feature_names_out()
    themes_per_bank[bank] = list(keywords)

# Save themes
themes_df = pd.DataFrame([
    {"bank": bank, "top_keywords": ", ".join(keywords)}
    for bank, keywords in themes_per_bank.items()
])
themes_df.to_csv("data/processed/review_themes.csv", index=False)

# -------------------------
# 4. Visualizations
# -------------------------

# Sentiment distribution per bank
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sentiment_label', hue='bank')
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.legend(title='Bank')
plt.tight_layout()
plt.savefig("data/processed/sentiment_distribution.png")
plt.close()

# WordCloud per bank
for bank in df['bank'].unique():
    text = " ".join(df[df['bank'] == bank]['review'].astype(str))
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"WordCloud for {bank}")
    plt.tight_layout()
    plt.savefig(f"data/processed/{bank}_wordcloud.png")
    plt.close()

print("Sentiment analysis and thematic extraction completed!")
print("CSV and plots saved to data/processed/")
