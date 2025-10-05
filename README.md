🛰️ OSINT Lab 7 – Automated Social Media OSINT Pipeline
📘 Project Overview

This project implements an automated OSINT (Open-Source Intelligence) pipeline that collects, processes, and analyzes social media data from multiple platforms, including Reddit and Twitter.

🚀 Features

🌐 Multi-platform data collection (Reddit & Twitter)

🧹 Automated data cleaning and preprocessing

🧠 Sentiment analysis using TextBlob

📈 Word cloud and sentiment visualization

💾 SQLite database storage

⚡ Simple setup with .env for API keys

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Mathewsunil24/osint_7.git
cd osint_7

2️⃣ Create Virtual Environment
python -m venv osint_env


Activate it:

Windows

osint_env\Scripts\activate


Linux/Mac

source osint_env/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in your project folder and add your keys:

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
TWITTER_BEARER_TOKEN=your_twitter_bearer_token

5️⃣ Run the Pipeline
python main.py

🔑 API Keys Required

🐦 Twitter API Bearer Token

👽 Reddit Client ID and Secret

⚠️ Note: Make sure your API credentials are stored safely in the .env file and never shared publicly.

📂 Project Structure
osint_pipeline/
├── collectors/          # Platform-specific data collectors
├── utils/               # Visualization and helper scripts
├── data/                # Database and generated images
├── main.py              # Main pipeline
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

📊 Output

After successful execution:

Reddit and Twitter data are stored in data/

Generated visualizations:

reddit_wordcloud.png, reddit_sentiment.png

twitter_wordcloud.png, twitter_sentiment.png
