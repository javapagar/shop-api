from typing import Annotated
from pydantic import BaseModel, BeforeValidator
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

def get_password_hash(value:str) -> str:  
    return password_hash.hash(value)

class PasswordHashValue(BaseModel):
    value: Annotated[str, BeforeValidator(get_password_hash)]

    def verify_password(self, plain_value) -> bool:
        return password_hash.verify(plain_value, self.value)