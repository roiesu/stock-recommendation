import sqlite3
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.utilities.constants import DB_PATH

def insert_dummy_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            ticker TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    dummy_rows = [
        ('AAPL', '2025-05-16 13:00:00+00:00', 210.0),
        ('AAPL', '2025-05-16 13:05:00+00:00', 208.0),
        ('AAPL', '2025-05-16 13:10:00+00:00', 205.0),
        ('AAPL', '2025-05-16 13:15:00+00:00', 202.0),
        ('AAPL', '2025-05-16 13:20:00+00:00', 198.0),
        ('AAPL', '2025-05-16 13:25:00+00:00', 203.0),
        ('AAPL', '2025-05-16 13:30:00+00:00', 206.0),
        ('AAPL', '2025-05-16 13:35:00+00:00', 209.0),
        ('AAPL', '2025-05-16 13:40:00+00:00', 206.0),
        ('AAPL', '2025-05-16 13:45:00+00:00', 208.0),
    ]

    cursor.executemany(
        "INSERT INTO prices (ticker, timestamp, price) VALUES (?, ?, ?)",
        dummy_rows
    )

    conn.commit()
    conn.close()
    print(f"Inserted {len(dummy_rows)} dummy rows into {DB_PATH}")

if __name__ == "__main__":
    insert_dummy_data()
