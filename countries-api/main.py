from typing import Union

from fastapi import FastAPI

from handlers import get_response

app = FastAPI()

@app.get("/")
def read_root():
    return get_response()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}