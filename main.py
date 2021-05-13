from fastapi import FastAPI, Response, Header
from schemas import *
from typing import Optional

app = FastAPI()


@app.get("/get-number", tags=["public"], response_model=Num)
async def get_num(num: int):
    resp_str = f"Ваше число {num}"
    return resp_str


@app.post("/test-post", tags=["public"])
async def post_mthd(headers: Optional[str] = Header("bearer 123")):
    headers = {"headers": headers}
    return Response(headers=headers)


@app.post("/post-json/item", tags=["public"], response_model=Item)
async def send_json(item: Item):
    return item
