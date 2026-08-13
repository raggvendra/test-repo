import requests

response = requests.get("https://dummyjson.com/quotes/random")

if response.status_code == 200:
    data = response.json()
    print("--- Quote of the Day ---")
    print(f'"{data["quote"]}"')
    print(f'- {data["author"]}')
else:
    print("Failed to retrieve quote.")
