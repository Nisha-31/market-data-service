import yfinance as yf
from datetime import datetime
import uuid
from app.core.database import SessionLocal
from app.models.price_point import PricePoint

# ✅ Fetch latest price using yfinance
def fetch_latest_price(symbol: str):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if data.empty:
        return None
    latest_price = data["Close"].iloc[-1]
    return {
        "symbol": symbol,
        "price": float(latest_price),
        "timestamp": datetime.utcnow(),
        "provider": "yfinance"
    }

# ✅ Store price in SQLite DB
def save_price_to_db(symbol: str, price: float):
    db = SessionLocal()
    db.add(PricePoint(symbol=symbol, price=price, timestamp=datetime.utcnow()))
    db.commit()
    db.close()

# ✅ Called by /prices/latest
def get_latest_price(symbol: str):
    db = SessionLocal()
    result = db.query(PricePoint).filter_by(symbol=symbol).order_by(PricePoint.timestamp.desc()).first()
    db.close()
    if result:
        return {
            "symbol": result.symbol,
            "price": result.price,
            "timestamp": result.timestamp,
            "provider": "yfinance"
        }
    return None

# ✅ Called by /prices/poll
def start_polling_job(symbols: list, interval: int, provider: str):
    for symbol in symbols:
        data = fetch_latest_price(symbol)
        if data:
            save_price_to_db(symbol, data["price"])

    job_id = f"poll_{uuid.uuid4().hex[:6]}"
    return {
        "job_id": job_id,
        "status": "accepted",
        "config": {
            "symbols": symbols,
            "interval": interval,
            "provider": provider
        }
    }
