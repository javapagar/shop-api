from src.users.domain.user import User
from tests.users.domain.user_const import (
    USER_ENABLE,
    USER_ID,
    USER_EMAIL,
    USER_PASSWORD,
    USER_SHOPPING_CART_ID,
)


class UserBuilder:
    def __init__(self):
        self._uuid = USER_ID
        self._email = USER_EMAIL
        self._password = USER_PASSWORD
        self._enable = USER_ENABLE
        self._shopping_cart_uuid = USER_SHOPPING_CART_ID

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

    def with_shopping_cart_id(self, shopping_cart_id: int) -> "UserBuilder":
        self._shopping_cart_uuid = shopping_cart_id
        return self

    def build(self) -> User:
        return User(
            uuid=self._uuid,
            email=self._email,
            password=self._password,
            enable=self._enable,
            shopping_cart_uuid=self._shopping_cart_uuid,
        )
