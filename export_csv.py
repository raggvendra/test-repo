import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, quote, author, saved_at FROM quotes")
    rows = cursor.fetchall()

    if not rows:
        print("No records found in quotes.db to export.")
        conn.close()
        return

    filename = "quotes_export.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Quote", "Author", "Saved At"])
        writer.writerows(rows)

    print("--- Export Successful ---")
    print(f"Exported {len(rows)} records to '{filename}'")

    conn.close()

if __name__ == "__main__":
    export_to_csv()
