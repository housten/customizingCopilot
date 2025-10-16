# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example Pydantic model
data_store = {}

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

@app.get("/items", response_model=List[Item])
def get_items():
    return list(data_store.values())

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return data_store[item_id]

@app.post("/items", response_model=Item)
def create_item(item: Item):
    data_store[item.id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    data_store[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del data_store[item_id]
    return {"ok": True}
