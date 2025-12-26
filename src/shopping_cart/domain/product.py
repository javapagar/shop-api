

from pydantic import BaseModel, BeforeValidator
from typing import Annotated
from uuid import UUID

def check_uuid(value:str):
    uuid_object = UUID(hex=value)

    return uuid_object.hex

class Product(BaseModel):
    uuid: Annotated[str,BeforeValidator(check_uuid)]
    name:str
    quantity:int
    price:float
