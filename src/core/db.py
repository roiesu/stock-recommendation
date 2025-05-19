import sqlite3
from datetime import datetime, timedelta, timezone
from src.utilities.constants import DB_PATH

def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_ticker_timestamp
        ON prices (ticker, timestamp DESC)
    """)
    conn.commit()


def save_prices(conn, prices):
    conn.executemany(
        "INSERT INTO prices (ticker, timestamp, price) VALUES (?, ?, ?)",
        [(p["ticker"], p["timestamp"], p["price"]) for p in prices]
    )
    conn.commit()

def cleanup_old_data(conn):
    three_days_ago = datetime.now(timezone.utc) - timedelta(days=3)
    conn.execute("DELETE FROM prices WHERE timestamp < ?", (three_days_ago,))
    conn.commit()

def get_prices_for_ticker(ticker: str) -> list[float]:
    try:
        conn = sqlite3.connect(DB_PATH)
        init_db(conn)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT price FROM prices
            WHERE ticker = ?
            ORDER BY timestamp DESC
        """, (ticker,))
        rows = cursor.fetchall()
        conn.close()
        return [float(row[0]) for row in rows]

    except Exception as e:
        print(f"DB error: {e}")
        raise

