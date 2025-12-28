from uuid import uuid4

from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository


class UserSaver:
    def __init__(self, saver: UserRepository):
        self.saver = saver

    def save(self, email: str, password: str, enable: bool = True) -> str:
        uuid = uuid4().hex
        shoping_cart_uuid = uuid4().hex
        user = User(
            uuid=uuid,
            email=email,
            password=password,
            enable=enable,
            shopping_cart_uuid=shoping_cart_uuid,
        )
        self.saver.save(user)
        return uuid
