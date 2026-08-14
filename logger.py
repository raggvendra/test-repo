import requests
import json
from datetime import datetime

# 1. Fetch live API data
response = requests.get("https://dummyjson.com/quotes/random")

if response.status_code == 200:
    data = response.json()
    
    # 2. Format entry with timestamp
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "quote": data["quote"],
        "author": data["author"]
    }

    # 3. Read existing history or initialize empty list
    try:
        with open("quotes_history.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    # 4. Append new entry and save back to file
    history.append(entry)

    with open("quotes_history.json", "w") as f:
        json.dump(history, f, indent=2)

    print("--- New Entry Saved to File ---")
    print(f'Quote: "{entry["quote"]}"')
    print(f'Author: {entry["author"]}')
    print(f'Saved at: {entry["timestamp"]}')
    print(f'Total Saved Entries: {len(history)}')

else:
    print("Failed to fetch data from API.")
