from pydantic import BaseModel, BeforeValidator, RootModel
from typing import Annotated
from uuid import UUID


def check_uuid(value:str) ->str:
    UUID(value)
    return value


class UUIDValue(RootModel):
    root: Annotated[str, BeforeValidator(check_uuid)]
