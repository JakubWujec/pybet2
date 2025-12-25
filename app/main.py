from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel
from app.routers.api import router
from app.db_session import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before
    create_db_and_tables()

    print("READY TO LAUNCH")
    yield

    # cleanup after


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
