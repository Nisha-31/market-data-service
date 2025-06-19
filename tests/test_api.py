import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_latest_price():
    response = client.get("/prices/latest?symbol=AAPL")
    assert response.status_code == 200 or response.status_code == 404


def test_post_polling():
    payload = {
        "symbols": ["AAPL", "MSFT"],
        "interval": 60,
        "provider": "yfinance"
    }
    response = client.post("/prices/poll", json=payload)
    assert response.status_code == 202
    data = response.json()
    assert "job_id" in data