import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def auth():
    pass
