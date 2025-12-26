from pydantic import BaseModel, Field
from typing import Annotated


class ProductRequest(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    quantity: Annotated[int, Field(default=1)]
    price: float
