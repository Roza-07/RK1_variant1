"""Задание 3: API создания товара при помощи FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="РК №1 — Вариант 1")


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    tags: list[str] = Field(default_factory=list)


class ItemResponse(Item):
    id: int


next_id = 1


@app.post("/items", response_model=ItemResponse)
def create_item(item: Item) -> ItemResponse:
    global next_id
    result = ItemResponse(id=next_id, **item.model_dump())
    next_id += 1
    return result
