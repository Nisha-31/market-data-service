from pydantic import BaseModel
from typing import List
from datetime import datetime

class PriceResponse(BaseModel):
    symbol: str
    price: float
    timestamp: datetime
    provider: str

class PollRequest(BaseModel):
    symbols: List[str]
    interval: int
    provider: str

class PollResponse(BaseModel):
    job_id: str
    status: str
    config: dict

class AverageResponse(BaseModel):
    symbol: str
    average_price: float
    timestamp: datetime