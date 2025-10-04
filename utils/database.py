import sqlite3
import os

# Path to store the database
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "osint_pipeline.db")

# Ensure the data folder exists
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(posts):
    if not posts:
        print("No posts to save.")
        return

    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for post in posts:
        c.execute(
            "INSERT INTO posts (text, sentiment) VALUES (?, ?)",
            (post["text"], post["sentiment"])
        )
    conn.commit()
    conn.close()
    print(f"✅ Saved {len(posts)} posts to database: {DB_FILE}")

def load_from_db():
    if not os.path.exists(DB_FILE):
        print("Database not found.")
        return []

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT text, sentiment FROM posts")
    rows = c.fetchall()
    conn.close()
    return [{"text": row[0], "sentiment": row[1]} for row in rows]
