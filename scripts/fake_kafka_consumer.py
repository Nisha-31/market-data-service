import sqlite3
from statistics import mean
from datetime import datetime
from sqlalchemy.orm import Session
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import SessionLocal
from app.models.moving_average import MovingAverage

def fetch_prices(symbol):
    conn = sqlite3.connect("market.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT price FROM price_points WHERE symbol = ? ORDER BY timestamp DESC LIMIT 5",
        (symbol,)
    )
    prices = [row[0] for row in cursor.fetchall()]
    conn.close()
    return prices

def compute_and_store_moving_average(symbol):
    prices = fetch_prices(symbol)
    if len(prices) < 5:
        print(f" Not enough price points for {symbol}. Found: {len(prices)}")
        return

    average = round(mean(prices), 2)

    # Store in DB
    db: Session = SessionLocal()
    ma = MovingAverage(symbol=symbol, average_price=average, timestamp=datetime.utcnow())
    db.add(ma)
    db.commit()
    db.close()

    print(f"✅ Stored 5-point moving average for {symbol}: {average}")


if __name__ == "__main__":
    compute_and_store_moving_average("AAPL")
