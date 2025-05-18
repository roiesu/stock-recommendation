import yfinance as yf
from datetime import datetime, timedelta
from db import init_db, save_prices, cleanup_old_data

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA"]

def is_trading_hours():
    now = datetime.now()
    return now.weekday() < 5 and (
        (now.hour == 13 and now.minute >= 30) or (14 <= now.hour < 20)
    )

def fetch_prices():
    prices = []
    now = datetime.now()

    for ticker in tickers:
        current_ticker = yf.download(ticker, interval="5m", start=now - timedelta(minutes=10), end=now, progress=False)
        if not current_ticker.empty:
            last = current_ticker.iloc[-1]
            prices.append({
                "ticker": ticker,
                "timestamp": last.name.to_pydatetime(),
                "price": round(last["Close"], 2)
            })
    return prices

def run():
    if not is_trading_hours():
        print("Outside of trading hours")
        return

    init_db()
    prices = fetch_prices()
    if prices:
        save_prices(prices)
        cleanup_old_data()
    else:
        print("No data")

if __name__ == "__main__":
    run()