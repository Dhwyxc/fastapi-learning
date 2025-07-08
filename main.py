from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.util.init_db import init_db
from contextlib import asynccontextmanager
from app.routers.auth import auth_router
from app.util.protectRouter import get_current_user
from app.db.schema.user import UserOutput

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database when the application starts."""
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/protected")
def protected_route(current_user: UserOutput = Depends(get_current_user)):
    """A protected route that requires authentication."""
    return {"data": current_user}

@app.get("/")
def read_root():
    return {"data": "Hello World"}

