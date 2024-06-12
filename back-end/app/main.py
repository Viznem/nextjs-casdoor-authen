import os

from starlette.middleware.sessions import SessionMiddleware

from config.database import Base, engine

from config import config
from functools import lru_cache
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import api

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Social Network App - Agest Training",
    description="This app for purples of training Agest company",
    version="0.1.0",
)

app.include_router(api.route)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.urandom(24),
    session_cookie="fastapi-session",
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
