import requests
from bs4 import BeautifulSoup

def fetch_reddit(topic="technology", limit=5):
    url = f"https://www.reddit.com/r/{topic}/top/?t=day"
    headers = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")

    posts = []
    for post in soup.find_all("h3")[:limit]:
        posts.append({
            "platform": "reddit",
            "user": "anonymous",
            "timestamp": "N/A",
            "text": post.get_text(),
            "url": url
        })
    return posts
