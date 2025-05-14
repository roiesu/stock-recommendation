import sqlite3
from datetime import datetime, timedelta

DB_PATH = "stock_data.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                ticker TEXT,
                timestamp DATETIME,
                price REAL
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prices ON prices (ticker, timestamp)")

def save_prices(prices):
    with sqlite3.connect(DB_PATH) as conn:
        for price in prices:
            conn.execute(
                "INSERT INTO prices (ticker, timestamp, price) VALUES (?, ?, ?)",
                (price["ticker"], price["timestamp"], price["price"])
            )

def cleanup_old_data():
    threshold = datetime.now() - timedelta(days=3)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM prices WHERE timestamp < ?", (threshold,))
