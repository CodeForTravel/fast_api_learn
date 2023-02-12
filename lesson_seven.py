"""
Path Parameters and Numeric Validations
"""
from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()

# parameter format
# param_name : param_type = param default value/declaration
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(default=3,title="Item id to get item details"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Order the parameters as you need
@app.get("/random-order-paramerter/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Order the parameters as you need, tricks
@app.get("/order-parameter-tricks/{item_id}/")
async def order_parameter(*, q:str, item_id:int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Number validations: greater than or equal
@app.get("/number-validation-gt/{item_id}/")
async def numbar_validation_gt(*, item_id:int = Path(title="Item ID", ge=3, le=1000), q:str=None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results