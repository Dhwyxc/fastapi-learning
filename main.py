from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from app.util.init_db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database when the application starts."""
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

