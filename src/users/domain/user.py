from pydantic import BaseModel, Field

from typing import Annotated

class User(BaseModel):
    uuid: str
    email: str
    pasword: str
    enable: Annotated[bool, Field(default=True)]