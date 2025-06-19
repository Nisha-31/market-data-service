from sqlalchemy import Column, String, Float, DateTime, Index
from datetime import datetime
from app.core.database import Base

class MovingAverage(Base):
    __tablename__ = "moving_averages"

    symbol = Column(String, primary_key=True)
    timestamp = Column(DateTime, primary_key=True, default=datetime.utcnow)
    average_price = Column(Float)

    __table_args__ = (
        Index("ix_ma_symbol_timestamp", "symbol", "timestamp"),  
    )
