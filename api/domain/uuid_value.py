from pydantic import BaseModel, BeforeValidator
from typing import Annotated
from uuid import UUID


def check_uuid(value:str) ->str:
    UUID(value)
    return value


class UUIDValue(BaseModel):
    uuid: Annotated[str, BeforeValidator(check_uuid)]
