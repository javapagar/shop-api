from pydantic import BaseModel, Field, RootModel
from typing import Annotated

from src.products.domain.product import Product


class CartProductList(RootModel[list[Product]]):
    root: Annotated[list[Product], Field(default_factory=list)]


class ShoppingCart(BaseModel):
    content: Annotated[CartProductList, Field(default_factory=CartProductList)]
    cart_uuid: str
