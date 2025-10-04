import os
import praw
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit(subreddit_name, limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.new(limit=limit):
        posts.append({"text": submission.title + " " + submission.selftext})
    return posts
