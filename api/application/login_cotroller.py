from datetime import datetime, timedelta, timezone
import os
from typing import Optional

import jwt
from pwdlib import PasswordHash

from api.domain.env_vars import ALGORITHM, PATH_USER, SECRET_KEY
from api.domain.user_response import UserResponse
from src.users.application.user_searcher import UserSearcher
from src.users.infrastructure.in_file_user_repository import InFileUserRepository


class LoginCotroller:
    def __init__(self):
        self._user_repository = InFileUserRepository(PATH_USER)
        self._password_hash = PasswordHash.recommended()

    def login(self, email: str, password: str) -> Optional[UserResponse]:
        user_searcher = UserSearcher(self._user_repository)

        user_found = user_searcher.search(email)

        if user_found is not None and self.__verify_password(
            password, user_found.get("password")
        ):
            return UserResponse(
                email=user_found.get("email"),
                password="*****",
                shopping_cart_uuid=user_found.get("shopping_cart_uuid"),
            )

    def __verify_password(self, plain_value, hashed_value) -> bool:
        return self._password_hash.verify(plain_value, hashed_value)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return encoded_jwt
    
    def decode_user(self, token:str) -> UserResponse:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return UserResponse(**payload)
