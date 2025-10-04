import os
import praw
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Reddit credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API client (no login needed)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit(subreddit_name, limit=5):
    """Fetch latest posts from a subreddit"""
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    print(f"🔍 Fetching latest {limit} posts from r/{subreddit_name}...")
    for submission in subreddit.new(limit=limit):
        posts.append({"text": submission.title + " " + submission.selftext})
        print(f"📄 {submission.title}")
    print(f"✅ Fetched {len(posts)} posts from r/{subreddit_name}.")
    return posts
