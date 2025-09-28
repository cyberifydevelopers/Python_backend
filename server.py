from fastapi import FastAPI
from config.database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}