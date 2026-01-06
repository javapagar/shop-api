import os

from api.domain.env_vars import PATH_USER
from api.domain.password_hash import PasswordHashValue
from api.domain.user_response import UserResponse
from src.users.application.user_saver import UserSaver
from src.users.application.user_searcher import UserSearcher
from src.users.infrastructure.in_file_user_repository import InFileUserRepository

class UsersController:
    def __init__(self):
        self._user_repository = InFileUserRepository(PATH_USER)

    
    def save_user(self, email:str, password:str) -> str:
        saver = UserSaver(self._user_repository)
        password_hash_value = PasswordHashValue(value=password)
        return saver.save(email, password_hash_value.value)
    

    def get_user_info(self, email:str) -> UserResponse:
        searcher = UserSearcher(self._user_repository)

        user = searcher.search(email)
        
        return UserResponse(
            email=user.get("email"),
            password="****",
            shopping_cart_uuid=user.get("shopping_cart_uuid")
        )