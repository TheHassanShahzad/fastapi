from fastapi import FastAPI
from datetime import datetime

import os

# Retrieve the API key from environment variables
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/time")
def get_time():
    now = datetime.utcnow()
    return {"current_time_utc": now.isoformat()}

@app.get("/key")
def read_keyt():
    return {"key": openai_api_key}