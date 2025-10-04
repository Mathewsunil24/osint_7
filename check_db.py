import sqlite3
from tabulate import tabulate  # optional, for pretty printing

# Path to your database
db_path = "data/osint_pipeline.db"

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# Fetch all posts from the 'posts' table
cursor.execute("SELECT * FROM posts;")
rows = cursor.fetchall()

if rows:
    # Print in a nice table format
    print("\nAll posts in 'posts' table:")
    print(tabulate(rows, headers=["ID", "Text", "Sentiment"], tablefmt="fancy_grid"))
else:
    print("\nNo posts found in the database.")

# Close connection
conn.close()

