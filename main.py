from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/time")
def get_time():
    now = datetime.utcnow()
    return {"current_time_utc": now.isoformat()}
