import os
import time
import tweepy
import json
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize client
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

DATA_FILE = "data/twitter_results.json"

def fetch_twitter(query, max_tweets=5):
    tweets = []
    next_token = None
    remaining = max_tweets

    while remaining > 0:
        try:
            # Fetch tweets
            response = client.search_recent_tweets(
                query=query,
                tweet_fields=["text", "created_at"],
                max_results=min(100, remaining),
                next_token=next_token
            )

            if not response.data:
                break

            for tweet in response.data:
                tweets.append({"text": tweet.text})
                remaining -= 1
                if remaining <= 0:
                    break

            # Pagination
            next_token = response.meta.get("next_token")
            if not next_token:
                break

        except tweepy.TooManyRequests as e:
            # Rate limit exceeded, wait and retry
            reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
            sleep_seconds = max(reset_time - int(time.time()), 60)
            print(f"Rate limit exceeded. Sleeping for {sleep_seconds} seconds...")
            time.sleep(sleep_seconds)
            continue
        except Exception as e:
            print(f"Twitter API Error: {e}")
            break

    # Save to JSON
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved {len(tweets)} tweets to {DATA_FILE}")
    return tweets
