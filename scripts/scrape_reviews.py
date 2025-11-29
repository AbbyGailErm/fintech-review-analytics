from google_play_scraper import reviews, Sort
import pandas as pd

# List of banks and their app package names
apps = {
    "CBE": "com.combanketh.mobilebanking",  # Replace with actual package names
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, package_name in apps.items():
    print(f"Scraping reviews for {bank}...")
    result, _ = reviews(
        package_name,
        lang='en',  # Use English reviews
        country='ET',  # Ethiopia
        count=400,  # minimum 400 reviews per bank
        sort=Sort.NEWEST  # get latest reviews
    )

    for r in result:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

# Save raw data
df = pd.DataFrame(all_reviews)
df.to_csv("data/raw/reviews_raw.csv", index=False)
print("Scraping completed! Saved to data/raw/reviews_raw.csv")
