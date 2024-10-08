from fastapi import FastAPI
from handlers import get_response
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return get_response()