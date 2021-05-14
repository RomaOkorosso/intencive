from fastapi import FastAPI, Response, Header
from schemas import *
from typing import Optional

app = FastAPI()


@app.get("/get-sum", tags=["public"], response_model=Num)
async def get_num(first_num: int, second_num: int):
    resp_str = f"Сумма чисел {first_num + second_num}"
    return resp_str


@app.post("/test-post", tags=["public"])
async def post_mthd(headers: Optional[str] = Header("bearer 123")):
    headers = {"headers": headers}
    return Response(headers=headers)


@app.post("/post-json/item", tags=["public"], response_model=Item)
async def send_json(item: Item):
    return item
