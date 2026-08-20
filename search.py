import json
import sys

def search_quotes(keyword):
    try:
        with open("quotes_history.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No quote history found. Run logger.py first!")
        return

    keyword_lower = keyword.lower()
    matches = [
        q for q in history 
        if keyword_lower in q["quote"].lower() or keyword_lower in q["author"].lower()
    ]

    print(f"--- Search Results for '{keyword}' ({len(matches)} found) ---")
    if not matches:
        print("No matching entries found.")
        return

    for idx, entry in enumerate(matches, 1):
        print(f"\n[{idx}] Saved at: {entry['timestamp']}")
        print(f'    Quote: "{entry["quote"]}"')
        print(f'    Author: {entry["author"]}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_term = " ".join(sys.argv[1:])
    else:
        search_term = input("Enter keyword or author to search: ")
    
    search_quotes(search_term)
