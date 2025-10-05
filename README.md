# 🕵️‍♂️ OSINT Lab 7 - Automated Social Media OSINT Pipeline

## 📘 Project Overview
This project implements an **automated OSINT (Open Source Intelligence) pipeline** that collects, analyzes, and visualizes social media data from multiple platforms such as **Reddit** and **Twitter**.  
It performs sentiment analysis, generates word clouds, and stores results for further investigation.

---

## 🚀 Features
- 🌐 Multi-platform data collection (Reddit, Twitter)
- 🧹 Automated data cleaning and preprocessing
- 💬 Sentiment analysis using TextBlob
- 📊 Data visualization with word clouds and sentiment charts
- 💾 Local data storage in JSON format
- 🔄 Modular structure for easy updates and debugging

---

## 🧰 Project Structure
osint_pipeline/
├── collectors/ # Reddit and Twitter data collectors
│ ├── reddit_collector.py
│ ├── twitter_collector.py
│
├── utils/ # Processing and visualization scripts
│ ├── data_cleaner.py
│ ├── visualize.py
│
├── data/ # Contains collected and processed data
│ ├── reddit_results.json
│ ├── twitter_results.json
│ ├── reddit_wordcloud.png
│ ├── reddit_sentiment.png
│ ├── twitter_wordcloud.png
│ ├── twitter_sentiment.png
│
├── main.py # Main pipeline file
├── requirements.txt # Dependencies list
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Mathewsunil24/osint_7.git
cd osint_pipeline
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv osint_env
osint_env\Scripts\activate   # On Windows
# or
source osint_env/bin/activate   # On Linux/Mac
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the root folder and add your API keys:

ini
Copy code
REDDIT_CLIENT_ID=your_client_id
REDDIT_SECRET=your_secret
REDDIT_USER_AGENT=your_user_agent

TWITTER_BEARER_TOKEN=your_bearer_token
5️⃣ Run the Pipeline
bash
Copy code
python main.py
🔑 API Keys Required
Reddit API: Client ID, Secret, and User Agent

Twitter API: Bearer Token

(Optional) You can reduce the number of tweets fetched in twitter_collector.py to avoid rate-limit issues.

🧠 How It Works
Data Collection – Collects posts and tweets using Reddit and Twitter APIs.

Processing – Cleans text, removes duplicates and unwanted symbols.

Sentiment Analysis – Classifies content as Positive, Negative, or Neutral using TextBlob.

Visualization – Generates:

📈 Sentiment distribution chart

☁️ WordCloud for top words

Storage – Saves outputs in /data folder for review.

📸 Sample Outputs
Platform	Word Cloud	Sentiment Graph
Reddit		
Twitter	

🧩 Technologies Used
🐍 Python 3

🌍 PRAW (Reddit API Wrapper)

🐦 Tweepy (Twitter API Wrapper)

🧠 TextBlob for sentiment analysis

🎨 Matplotlib & WordCloud for visualization

💾 JSON & SQLite for data handling
