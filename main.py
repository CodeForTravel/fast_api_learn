from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from models.enum import ModelName
from starlette.requests import Request
app = FastAPI()


# define model
class Product(BaseModel):
    name : str
    price : float
    is_active : Union[bool, None] = None

@app.get("/")
async def root_method():
    response = {
        "message":"Bismillah!"
    }
    return response

item_list = {
        1:{"id":1, "message":"Message 1"},
        2:{"id":2, "message":"Message 2"},
        3:{"id":3, "message":"Message 3"},
        4:{"id":4, "message":"Message 4"},
    }

@app.get("/items")
async def read_item_list():
    return item_list


@app.get("/items/{item_id}")
async def read_item_detail(item_id: int, search: Union[str, None] = None):
    item = item_list.get(item_id)
    return {"item_id": item_id, "item":item}


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id, "price":product.price}

# =================== path parameter example =====================
# path Order matters 
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Predefined values 
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    resp = {"model_name": model_name, "message": "Have some residuals"}
    if model_name is ModelName.alexnet:
        resp = {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "lenet":
        resp = {"model_name": model_name, "message": "LeCNN all the images"}
    return resp

# Path parameters containing paths 
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# =================== Query Parameters example =====================
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/query-params/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/optional-query-params/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/bool-query-params/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Multiple path and query parameters
# You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
# And you don't have to declare them in any specific order.
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    item_id: int, user_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# undefined query params
@app.get("/undefined_query_param/")
async def undefined_query_param(request: Request):
    query_params = request.query_params
    query_param_value = query_params.get("param_name")
    return {"param_name": query_param_value}