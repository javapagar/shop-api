from abc import ABC, abstractmethod
from typing import Optional

from src.users.domain.user import User


class  UserRepository:
    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def find(Self, id: str) -> Optional[User]: ...
