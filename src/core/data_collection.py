from datetime import datetime, timedelta, timezone
from src.core.db import init_db, save_prices, cleanup_old_data
from src.utilities.constants import TICKERS, DB_PATH
from src.utilities.time import is_trading_hours, get_data_interval
import yfinance as yf
import pandas as pd
import sqlite3

DEV_MODE = False
DB_PATH = "stock_data.db"

def is_trading_hours():
    if DEV_MODE:
        return True
    now = datetime.now(timezone.utc)
    return now.weekday() < 5 and (
        (now.hour == 13 and now.minute >= 30) or (14 <= now.hour < 20)
    )

def fetch_prices():
    prices = []    
    start, end = get_data_interval()

    for ticker in TICKERS:
        try:
            df = yf.download(
                ticker,
                interval="5m",
                start=start,
                end=end,
                progress=False
            )

            if df.empty:
                print(f"[{ticker}] No data in requested range")
                continue

            last = df.iloc[-1]
            time_stamp = pd.to_datetime(df.index[-1]).to_pydatetime()
            price = float(last["Close"].item())

            prices.append({
                "ticker": ticker,
                "timestamp": time_stamp,
                "price": price
            })

        except Exception as e:
            print(f"[{ticker}] Error while fetching/parsing: {e}")

    return prices

def run():
    if not is_trading_hours():
        print("Not in trading hours, skipping")
        return
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    prices = fetch_prices()
    if prices:
        save_prices(conn, prices)
        cleanup_old_data(conn)
        print(f"Saved {len(prices)} records")
    else:
        print("No valid prices collected")

    conn.close()
