import os
from dotenv import load_dotenv

load_dotenv()
SENTIMENT_API_KEY = os.getenv("SENTIMENT_API_KEY")

def add_sentiment(data):
    for item in data:
        # Placeholder: if you have a sentiment API, call it here
        item["sentiment"] = "neutral"
    return data
