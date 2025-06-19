from fastapi import APIRouter,  HTTPException
from app.schemas import PriceResponse, PollRequest, PollResponse, AverageResponse
from app.services.price_service import get_latest_price, start_polling_job
from app.services.price_service import fetch_latest_price, save_price_to_db, get_latest_price

from app.core.database import SessionLocal
from app.models.moving_average import MovingAverage

router = APIRouter()

@router.get("/prices/latest", response_model=PriceResponse)
def get_latest_price(symbol: str):
    data = fetch_latest_price(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    save_price_to_db(symbol, data["price"])
    return data

@router.post("/prices/poll", response_model=PollResponse, status_code=202)
def poll_prices(request: PollRequest):
    job_id = "poll_001"
    for symbol in request.symbols:
        data = fetch_latest_price(symbol)
        if data:
            save_price_to_db(symbol, data["price"])
    return {
        "job_id": job_id,
        "status": "accepted",
        "config": request.dict()
    }

@router.get("/averages/latest", response_model=AverageResponse)
def get_latest_average(symbol: str):
    db = SessionLocal()
    avg = db.query(MovingAverage).filter_by(symbol=symbol).order_by(MovingAverage.timestamp.desc()).first()
    db.close()
    if not avg:
        raise HTTPException(status_code=404, detail="Average not found")
    return avg