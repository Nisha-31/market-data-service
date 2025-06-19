from sqlalchemy import Column, String, Float, DateTime, Index
from app.core.database import Base

class PricePoint(Base):
    __tablename__ = "price_points"
    symbol = Column(String, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    price = Column(Float)
    provider = Column(String)

    __table_args__ = (
        Index("idx_symbol_timestamp", "symbol", "timestamp"),
    )
