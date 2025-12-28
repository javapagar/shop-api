from pydantic import BaseModel, Field
from typing import Annotated


class ShoppingCartProductRequest(BaseModel):
    shopping_cart_uuid: str
    name: Annotated[str, Field(min_length=2, max_length=100)]
    quantity: Annotated[int, Field(default=1)]
    price: float
