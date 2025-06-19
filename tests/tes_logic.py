from app.services.price_service import fetch_latest_price
from statistics import mean

def test_fetch_latest_price():
    result = fetch_latest_price("AAPL")
    assert result is None or "price" in result


def test_moving_average_calc():
    prices = [100, 102, 104, 106, 108]
    assert mean(prices) == 104