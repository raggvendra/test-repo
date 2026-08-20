import sqlite3
import sys

def search_db(keyword):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    # Query using SQL LIKE pattern matching
    query = "SELECT id, quote, author, saved_at FROM quotes WHERE quote LIKE ? OR author LIKE ?"
    pattern = f"%{keyword}%"
    cursor.execute(query, (pattern, pattern))
    results = cursor.fetchall()

    print(f"--- SQLite Results for '{keyword}' ({len(results)} found) ---")
    if not results:
        print("No matching records in quotes.db.")
    else:
        for row in results:
            print(f"\n[ID: {row[0]}] Saved at: {row[3]}")
            print(f'    Quote: "{row[1]}"')
            print(f'    Author: {row[2]}')

    conn.close()

if __name__ == "__main__":
    search_term = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter search term: ")
    search_db(search_term)
