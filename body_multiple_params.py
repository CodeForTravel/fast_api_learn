from typing import Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/multiple-body-params/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# Singular values in body
@app.put("singular-value-in-body")
async def singular_value_in_body(
    item_id:int,
    item:Item=None,
    user:User=None,
    extra_single_body_value:int=Body(gt=0),
    q: Union[str, None] = None
    ):
    results = {"item_id": item_id, "item": item, "user": user, "extra_single_body_value": extra_single_body_value}
    if q:
        results.update({"q": q})
    return results