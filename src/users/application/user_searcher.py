from typing import Any, Optional
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository


class UserSearcher:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def search(self, user_uuid: str) -> Optional[dict[str, Any]]:
        user = self._user_repository.find(user_uuid)

        if user is None:
            return None

        return user.model_dump()
