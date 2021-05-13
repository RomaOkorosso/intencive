# created by RomaOkorosso at 13.05.2021
# schemas.py

from pydantic import BaseModel


class Num(BaseModel):
    num: int

    class Config:
        orm_mode = True


class Item(BaseModel):
    id: int
    item_name: str
    item_description: str

    class Config:
        orm_mode = True
