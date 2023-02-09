from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

main_app = FastAPI()


# define model
class Product(BaseModel):
    name : str
    price : float
    is_active : Union[bool, None] = None

@main_app.get("/")
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

@main_app.get("/items")
async def read_item_list():
    return item_list


@main_app.get("/items/{item_id}")
async def read_item_detail(item_id: int, search: Union[str, None] = None):
    item = item_list.get(item_id)
    return {"item_id": item_id, "item":item}


@main_app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id, "price":product.price}