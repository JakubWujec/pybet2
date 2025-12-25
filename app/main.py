from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before

    print("READY TO LAUNCH")
    yield

    # cleanup after


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
