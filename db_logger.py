import sqlite3
import requests
from datetime import datetime

# 1. Connect to SQLite database (creates quotes.db if it doesn't exist)
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT NOT NULL,
        author TEXT NOT NULL,
        saved_at TEXT NOT NULL
    )
''')

# 3. Fetch live API data
response = requests.get("https://dummyjson.com/quotes/random")

if response.status_code == 200:
    data = response.json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 4. Insert data into SQLite database
    cursor.execute('''
        INSERT INTO quotes (quote, author, saved_at)
        VALUES (?, ?, ?)
    ''', (data["quote"], data["author"], now))

    conn.commit()

    # 5. Retrieve total row count
    cursor.execute("SELECT COUNT(*) FROM quotes")
    total_count = cursor.fetchone()[0]

    print("--- Entry Saved to SQLite Database ---")
    print(f'Quote: "{data["quote"]}"')
    print(f'Author: {data["author"]}')
    print(f'Saved at: {now}')
    print(f'Total DB Entries: {total_count}')

else:
    print("Failed to fetch data from API.")

conn.close()
