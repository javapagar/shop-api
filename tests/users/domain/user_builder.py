from src.users.domain.user import User
from tests.users.domain.user_const import (
    USER_ENABLE,
    USER_ID,
    USER_EMAIL,
    USER_PASSWORD,
)


class UserBuilder:
    def __init__(self):
        self._uuid = USER_ID
        self._email = USER_EMAIL
        self._password = USER_PASSWORD
        self._enable = USER_ENABLE

    def with_id(self, uuid: str) -> "UserBuilder":
        self._uuid = uuid
        return self

    def with_email(self, email: str) -> "UserBuilder":
        self._email = email
        return self

    def with_password(self, password: str) -> "UserBuilder":
        self._password = password
        return self

    def with_enable(self, enable: bool) -> "UserBuilder":
        self._enable = enable
        return self

    def build(self) -> User:
        return User(
            id=self._uuid,
            email=self._email,
            pasword=self._password,
            enable=self._enable,
        )
