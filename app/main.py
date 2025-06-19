from fastapi import FastAPI
from app.api.routes import router
import webbrowser

app = FastAPI()  
webbrowser.open("http://127.0.0.1:8000/docs")

app.include_router(router)
