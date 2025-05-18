from fastapi import FastAPI, HTTPException, Query
from src.core.db import get_prices_for_ticker
from src.core.cup_and_handle import detect_cup_and_handle
from decimal import Decimal
from src.utilities.constants import TICKERS

VALID_TICKERS = set(TICKERS)

app = FastAPI()

@app.get("/analyze")
def analyze(ticker: str = Query(..., description="Stock ticker to analyze")):
    ticker = ticker.upper()

    if ticker not in VALID_TICKERS:
        raise HTTPException(status_code=400, detail=f"Invalid ticker")

    try:
        print("enters")
        prices = get_prices_for_ticker(ticker)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from database")

    if not prices:
        raise HTTPException(status_code=404, detail=f"No data found for ticker: {ticker}")

    if len(prices) < 7:
        raise HTTPException(status_code=400, detail="Not enough data for pattern analysis")

    try:
        prices_decimal = [Decimal(str(p)) for p in prices]
        print(f"📊 Analyzing prices: {prices_decimal}")
        match = detect_cup_and_handle(prices_decimal)
    except Exception as e:
        print(f"❌ Pattern detection failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to analyze pattern")


    return {
        "ticker": ticker,
        "match": match
    }