import json
import os
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- Paths to data files ---
REDDIT_FILE = "data/reddit_results.json"
TWITTER_FILE = "data/twitter_results.json"

# --- Utility to load data ---
def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Data file not found: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# --- Utility to generate WordCloud ---
def generate_wordcloud(posts, title, output_file):
    if not posts:
        print(f"❌ No posts to generate WordCloud for {title}")
        return
    text = " ".join(post["text"] for post in posts)
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"WordCloud for {title}", fontsize=16)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"✅ WordCloud saved to {output_file}")

# --- Utility to plot sentiment bar chart ---
def plot_sentiment(posts, title, output_file):
    if not posts:
        print(f"❌ No posts to generate sentiment chart for {title}")
        return
    sentiments = [post.get("sentiment", "neutral") for post in posts]
    counter = Counter(sentiments)
    plt.figure(figsize=(6,4))
    plt.bar(counter.keys(), counter.values(), color=["green", "red", "gray"])
    plt.title(f"Sentiment Analysis for {title}", fontsize=14)
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"✅ Sentiment chart saved to {output_file}")

# --- Main ---
if __name__ == "__main__":
    # --- Reddit ---
    reddit_posts = load_data(REDDIT_FILE)
    generate_wordcloud(reddit_posts, "Reddit", "data/reddit_wordcloud.png")
    plot_sentiment(reddit_posts, "Reddit", "data/reddit_sentiment.png")

    # --- Twitter ---
    twitter_posts = load_data(TWITTER_FILE)
    generate_wordcloud(twitter_posts, "Twitter", "data/twitter_wordcloud.png")
    plot_sentiment(twitter_posts, "Twitter", "data/twitter_sentiment.png")
