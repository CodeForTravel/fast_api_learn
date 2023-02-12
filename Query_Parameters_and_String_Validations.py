"""

# parameter format
# param_name : param_type = param default value/declaration
"""

from typing import List, Union

from fastapi import FastAPI, Query
from pydantic import Required
app = FastAPI()


@app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None, max_length=10)):
async def read_items(q: str | None = Query(default=None, title="Query Title", description="Query string for the items to search in the database that have a good match", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Make it required
@app.get("/items-required/")
async def read_items(q: str = Query(default=...,min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Required with Ellipsis (...)
# @app.get("/items/")
# async def read_items(q: str = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Required with None
# You can declare that a parameter can accept None, but that it's still required. This would force clients to send a value, even if the value is None.
@app.get("/required_even_with_none/")
async def required_even_with_none(q: Union[str, None] = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Use Pydantic's Required instead of Ellipsis (...)
@app.get("/pydantic_required/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"pydantic_required": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter list / multiple values
@app.get("/parameter_list/")
async def parameter_list(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items

# Query parameter list / multiple values with defaults
@app.get("/parameter_list_with_defaults/")
async def parameter_list_with_defaults(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# Using list
@app.get("/parameter_list_using_list/")
async def parameter_list_using_list(q: list = Query(default=Required)):
    query_items = {"q": q}
    return query_items