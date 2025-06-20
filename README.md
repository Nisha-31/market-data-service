#  Market Data Microservice

A production-ready FastAPI microservice that fetches, stores, and processes market data (e.g., stock prices). It supports polling stock prices from providers like Yahoo Finance (`yfinance`), computes 5-point moving averages, and serves the data over REST APIs. Deployed on **Render** using **SQLite**, no Docker required.

---

##  Features

-  REST API with FastAPI
-  SQLite database using SQLAlchemy ORM
-  Fetch prices from `yfinance`
-  Compute and store 5-point moving averages
-  Kafka simulation using a Python script
-  Unit tests with `pytest`
-  Hosted on Render with GitHub integration

---

##  Tech Stack

- Python 3.8+
- FastAPI
- SQLite + SQLAlchemy
- yfinance (provider)
- Pytest
- Render (for deployment)

##  Project Structure

market-data-service/
├── app/
│ ├── api/ # FastAPI routes
│ ├── core/ # DB setup
│ ├── models/ # ORM models
│ ├── services/ # Business logic
│ └── main.py # App entrypoint
├── scripts/ # Kafka simulation scripts
├── tests/ # Unit tests
├── requirements.txt
├── README.md
└── .gitignore
  
##  Installation (Local)

```bash
git clone https://github.com/YOUR_USERNAME/market-data-service.git
cd market-data-service
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate (Windows)
pip install -r requirements.txt

 ## Running the App
1) uvicorn app.main:app --reload
2) POST /prices/poll
3)GET /prices/latest?symbol=AAPL

## Kafka Simulation (Consumer)
To simulate Kafka consumption and store moving averages:

python scripts/fake_kafka_consumer.py

## Run test:  pytest tests/

## Deployment on Render
1)Push code to GitHub
2)Create new Web Service on Render.com
3)Select your repo
4)Add build command: pip install -r requirements.txt     and   uvicorn app.main:app --host 0.0.0.0 --port 10000

Deploy!

 Live URL: https://market-data-service-xxxxx.onrender.com

Contact
Made by Nisha
🔗 GitHub: Nisha-31

Let me know if you'd like a downloadable `.md` file too!







