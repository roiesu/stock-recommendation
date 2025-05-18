import sqlite3

DB_PATH = "stock_data.db"

def inspect_latest(limit=10000):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Last {limit} records in 'prices' table:")
    cursor.execute("""
        SELECT ticker, timestamp, price
        FROM prices
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]:<6} | {row[1]} | ${row[2]}")
    
    conn.close()

if __name__ == "__main__":
    inspect_latest()
