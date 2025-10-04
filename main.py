import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from collectors.twitter_collector import fetch_twitter
from collectors.reddit_collector import fetch_reddit
from utils.cleaner import clean_text
from utils.database import save_to_db
from utils.sentiment import add_sentiment

def run_pipeline():
    data = []
    data.extend(fetch_twitter("AI", 5))
    data.extend(fetch_reddit("technology", 5))

    for d in data:
        d["text"] = clean_text(d["text"])

    data = add_sentiment(data)
    save_to_db(data)
    print(f"✅ Collected and saved {len(data)} posts.")

if __name__ == "__main__":
    run_pipeline()
