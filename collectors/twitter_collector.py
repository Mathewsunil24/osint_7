import os
from dotenv import load_dotenv
import requests

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def create_headers():
    return {"Authorization": f"Bearer {BEARER_TOKEN}"}

def fetch_twitter(keyword, limit=5):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={keyword}&max_results={limit}&tweet.fields=text"
    headers = create_headers()
    response = requests.get(url, headers=headers)
    tweets = []
    if response.status_code == 200:
        data = response.json()
        for tweet in data.get("data", []):
            tweets.append({"text": tweet["text"]})
    else:
        print(f"Twitter API Error {response.status_code}: {response.text}")
    return tweets
