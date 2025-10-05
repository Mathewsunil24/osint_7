🕵️‍♂️ OSINT Lab 7 - Automated Reddit & Twitter OSINT Pipeline
📘 Project Overview

This project implements an automated OSINT (Open Source Intelligence) pipeline that collects, processes, and analyzes public social media data from Reddit and Twitter.
It performs data cleaning, sentiment analysis, and visualization (WordCloud & Sentiment Graph), and stores all collected data in a SQLite database.

🚀 Features

✅ Reddit data collection using API
✅ Twitter data collection (with rate-limit handling)
✅ Sentiment analysis using TextBlob
✅ WordCloud generation from text data
✅ Sentiment visualization (Positive, Negative, Neutral)
✅ SQLite database integration for structured storage
✅ Easy modular structure (collectors, utils, data)

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Mathewsunil24/osint_8.git
cd osint_8/osint_pipeline

2️⃣ Create virtual environment
python -m venv osint_env
osint_env\Scripts\activate   # for Windows
# OR
source osint_env/bin/activate   # for Linux/Mac

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up environment variables

Create a .env file in your osint_pipeline/ folder with the following values:

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=your_app_name
TWITTER_BEARER_TOKEN=your_twitter_bearer_token

▶️ Run the Pipeline
Collect Reddit Data
python -m collectors.reddit_collector

Collect Twitter Data
python -m collectors.twitter_collector

Visualize Data (WordCloud + Sentiment Graph)
python -m utils.visualize

Check Database
python -m utils.db_viewer

🧩 Project Structure
osint_pipeline/
├── collectors/
│   ├── reddit_collector.py     # Reddit data collection
│   ├── twitter_collector.py    # Twitter data collection
│
├── utils/
│   ├── visualize.py            # WordCloud + Sentiment visualization
│   ├── db_viewer.py            # Check stored data in SQLite
│
├── data/
│   ├── reddit_results.json
│   ├── twitter_results.json
│   ├── osint_pipeline.db
│
├── main.py                     # Combined pipeline script
├── requirements.txt            # Dependencies
└── .env                        # API keys

🧠 Technologies Used

Python 3.x

PRAW – Reddit API wrapper

Requests / Tweepy – Twitter API access

TextBlob – Sentiment analysis

Matplotlib – Visualization

WordCloud – Word cloud generation

SQLite3 – Local database storage

📊 Output Samples

data/reddit_wordcloud.png → Word cloud from Reddit posts

data/reddit_sentiment.png → Sentiment analysis chart

data/twitter_wordcloud.png → Word cloud from Twitter tweets

data/twitter_sentiment.png → Twitter sentiment chart

⚠️ Notes

Twitter API may show “429 Too Many Requests” — this is a rate limit issue; try again later.

Make sure .env file is correctly filled before running any collector.

Reddit visualization works completely. Twitter visualization depends on successful API fetch.