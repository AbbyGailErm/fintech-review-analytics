import pandas as pd
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

# Load cleaned reviews
df = pd.read_csv("data/processed/reviews_clean.csv")

# 1️⃣ Sentiment Analysis using DistilBERT
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(review):
    result = sentiment_pipeline(review[:512])[0]  # limit to 512 tokens
    return result['label'], result['score']

df[['sentiment_label', 'sentiment_score']] = df['review'].apply(lambda x: pd.Series(get_sentiment(x)))

# 2️⃣ Thematic Analysis (Keyword Extraction)
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

df['clean_review'] = df['review'].apply(preprocess)

# TF-IDF for keyword extraction
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=100)
X = vectorizer.fit_transform(df['clean_review'])
keywords = vectorizer.get_feature_names_out()

# 3️⃣ Simple Theme Grouping (example)
# This is rule-based: group related keywords into themes
themes = {
    'User Interface & Experience': ['ui', 'design', 'navigation', 'layout'],
    'Transaction Performance': ['transfer', 'payment', 'slow', 'loading', 'crash'],
    'Account Access Issues': ['login', 'password', 'otp', 'authentication'],
    'Customer Support': ['support', 'help', 'service', 'response'],
    'Feature Requests': ['feature', 'add', 'request', 'update']
}

def assign_theme(review):
    assigned = []
    for theme, kw_list in themes.items():
        for kw in kw_list:
            if kw in review:
                assigned.append(theme)
                break
    return assigned if assigned else ['Other']

df['themes'] = df['clean_review'].apply(assign_theme)

# 4️⃣ Save results
df.to_csv("data/processed/reviews_with_sentiment_themes.csv", index=False)
print("Sentiment and thematic analysis completed! Saved to data/processed/reviews_with_sentiment_themes.csv")
