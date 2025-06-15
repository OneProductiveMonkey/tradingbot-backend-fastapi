import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Trading Bot API")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is live"}
