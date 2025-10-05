# **OSINT Lab 7 - Automated Social Media OSINT Pipeline**

## **Project Overview**
This project implements an automated OSINT pipeline that collects, processes, and analyzes social media data from multiple platforms including Reddit, GitHub, and Twitter.

## **Features**
- ✅ Multi-platform data collection:
  - Reddit
  - GitHub
  - Twitter
- ✅ Automated data cleaning and preprocessing
- ✅ Sentiment analysis using TextBlob
- ✅ SQLite database storage
- ✅ Scheduled automated collection

## **Setup Instructions**

### **1. Clone the repository**
```bash
git clone https://github.com/Mathewsunil24/osint_7.git
cd osint_pipeline
2. Create a virtual environment
bash
Copy code
python -m venv osint_env

# Activate the environment
# Linux/Mac
source osint_env/bin/activate

# Windows
osint_env\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up environment variables
bash
Copy code
cp sample.env.example .env
# Edit the .env file with your API keys
5. Run the pipeline
bash
Copy code
python main_safe.py
API Keys Required
🟢 Twitter API Bearer Token

🟢 Reddit Client ID and Secret

🟢 GitHub Personal Access Token (optional)

Project Structure
bash
Copy code
osint_pipeline/
├── collectors/          # Platform-specific data collectors
├── utils/               # Utilities for processing
├── data/                # Database and generated files
├── screenshots/         # Evidence screenshots
├── main_safe.py         # Main pipeline
└── requirements.txt     # Dependencies
Notes
Make sure your API keys are kept secret.

Ensure your virtual environment is activated before running scripts.

Use the data/ folder to check saved results, WordClouds, and sentiment charts.
