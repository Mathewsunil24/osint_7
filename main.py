import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import collectors
from collectors.reddit_collector import fetch_reddit
from collectors.twitter_collector import fetch_twitter

# Import utilities
from utils.cleaner import clean_text
from utils.database import save_to_db
from utils.sentiment import add_sentiment

def run_pipeline():
    data = []

    # ----- Reddit -----
    print("🔍 Fetching latest 5 posts from r/technology...")
    reddit_posts = fetch_reddit("technology", 5)
    print(f"✅ Fetched {len(reddit_posts)} posts from Reddit.")
    data.extend(reddit_posts)

    # ----- Twitter -----
    print("🔍 Fetching latest 3 tweets about AI...")
    twitter_posts = fetch_twitter("AI", 3)  # reduced number to avoid rate-limit
    print(f"✅ Fetched {len(twitter_posts)} tweets from Twitter.")
    data.extend(twitter_posts)

    # ----- Clean text -----
    for d in data:
        d["text"] = clean_text(d["text"])

    # ----- Sentiment Analysis -----
    data = add_sentiment(data)

    # ----- Save to DB -----
    save_to_db(data)
    print(f"✅ Collected and saved {len(data)} posts.")

if __name__ == "__main__":
    run_pipeline()
