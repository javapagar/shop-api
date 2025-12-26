from pydantic import BaseModel, Field

from src.shopping_cart.domain.product import Product


class ShoppingCart(BaseModel):
    content: list[Product] = Field(default_factory=list)
