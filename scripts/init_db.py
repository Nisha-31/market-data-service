import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.core.database import engine, Base
from app.models.price_point import PricePoint
from app.models.moving_average import MovingAverage 

# Create all tables
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
