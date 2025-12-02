# Customer Experience Analytics for Fintech Apps
A Real-World Data Engineering Challenge (Week 2)

This project analyzes Google Play Store reviews of three major Ethiopian banking apps:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to support Omega Consultancy by scraping reviews, analyzing customer sentiment, identifying themes, and storing results in a PostgreSQL database.

---

## 🔍 Project Objectives
1. Scrape at least 400 reviews per bank (1,200 total).
2. Clean and preprocess review text.
3. Perform sentiment analysis (DistilBERT, VADER, or TextBlob).
4. Extract themes and keywords (TF-IDF, spaCy).
5. Store processed data in PostgreSQL.
6. Generate insights and visualizations.
7. Deliver a 4–10 page stakeholder-friendly report.

---

## 📁 Repository Structure
fintech-review-analytics/
│
├─ data/
│ ├─ raw/ # Raw scraped CSVs
│ │ └─ reviews_raw.csv
│ ├─ processed/ # Cleaned and analyzed data + plots
│ │ ├─ reviews_clean.csv
│ │ ├─ reviews_with_sentiment.csv
│ │ ├─ review_themes.csv
│ │ ├─ sentiment_distribution.png
│ │ ├─ {Bank}_wordcloud.png
│ │ ├─ {Bank}_positive_wordcloud.png
│ │ ├─ {Bank}_negative_wordcloud.png
│ │ └─ task4_rating_vs_sentiment.png
│
├─ scripts/
│ ├─ scrape_reviews.py
│ ├─ preprocess_reviews.py
│ ├─ sentiment_thematic_analysis.py
│ └─ insert_to_postgres.py
│
├─ README.md
├─ requirements.txt
└─ .gitignore


---

## Setup & Requirements

**Python version:** 3.10+  
**Install dependencies:**  

```bash
pip install -r requirements.txt


PostgreSQL:

Ensure PostgreSQL is installed and running

Create a database named bank_reviews

Tables: banks and reviews

Workflow
1️⃣ Scrape Reviews
python3 scripts/scrape_reviews.py


Collects at least 400 reviews per bank (1,200 total)

Saves raw CSV in data/raw/reviews_raw.csv

2️⃣ Preprocess Reviews
python3 scripts/preprocess_reviews.py


Removes duplicates and missing values

Normalizes date format to YYYY-MM-DD

Saves cleaned CSV in data/processed/reviews_clean.csv

3️⃣ Sentiment & Thematic Analysis
python3 scripts/sentiment_thematic_analysis.py


Computes sentiment score & label (positive, neutral, negative)

Extracts top keywords/themes per bank using TF-IDF

Generates WordClouds for overall, positive, and negative reviews

Produces Task 4 visualizations: sentiment distribution, rating vs sentiment

Saves results in data/processed/

4️⃣ Store Data in PostgreSQL
python3 scripts/insert_to_postgres.py


Inserts banks and reviews into PostgreSQL tables

Maintains referential integrity (bank_id foreign key)

Insights & Recommendations

Drivers of Satisfaction: fast navigation, clean UI, convenient transactions

Pain Points: app crashes, slow transfers, login issues

Bank-specific Recommendations:

CBE: Improve transfer speed, reduce login errors

BOA: Fix crash bugs, enhance UI responsiveness

Dashen: Add biometric login, optimize transaction performance

Visualizations are included in data/processed/ to support insights.

Usage Notes

Run scripts in order:
scrape_reviews.py → preprocess_reviews.py → sentiment_thematic_analysis.py → insert_to_postgres.py

WordCloud generation may take a few seconds per bank.

Update insert_to_postgres.py with your PostgreSQL username/password if required.

Author

Abigail Biru

Project completed for Omega Consultancy Fintech Analytics Challenge – Week 2


---

You can just **copy this text** and replace your existing `README.md`.  

If you want, I can also make a **super-short “Quick Start” version** that only shows commands to run everything in order—great for graders. Do you want me to do that?

You said:
tes
ChatGPT said:

Great! Here’s a super-short “Quick Start” README you can use so someone can just follow commands and see everything run:

# Fintech Review Analytics – Quick Start

## Requirements
- Python 3.10+  
- PostgreSQL installed and running  
- Install Python dependencies:

```bash
pip install -r requirements.txt

Quick Run

Scrape reviews

python3 scripts/scrape_reviews.py


Preprocess reviews

python3 scripts/preprocess_reviews.py


Sentiment & thematic analysis + visualizations

python3 scripts/sentiment_thematic_analysis.py


Insert data into PostgreSQL

python3 scripts/insert_to_postgres.py

Notes

CSVs and plots are saved in data/processed/

PostgreSQL database: bank_reviews

Tables: banks, reviews



Abigail Biru



