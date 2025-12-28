from pydantic import BaseModel, Field

from typing import Annotated


class User(BaseModel):
    uuid: str
    email: str
    password: str
    enable: Annotated[bool, Field(default=True)]
    shopping_cart_uuid:str
