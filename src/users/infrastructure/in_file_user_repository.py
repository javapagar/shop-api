import pickle
import os

from src.users.domain.user_repository import UserRepository
from src.users.domain.user import User


class InFileUserRepository(UserRepository):
    def __init__(self, file_name: str):
        self._name = file_name
        self.__initialize()

    def save(self, user: User) -> None:
        user_list: list[User] = self.get_all()
        user_list.append(user)

        self.__save_list(user_list)

    def get_all(self) -> list[User]:
        with open(self._name, "rb") as file:
            user_list = pickle.load(file)
        return user_list

    def find_by_uuid(self, uuid: str) -> User:
        user_list = self.get_all()
        user_filtered: list = list(
            filter(lambda user: user if user.uuid == uuid else None, user_list)
        )
        if len(user_filtered) == 0:
            return None

        return user_filtered[0]
    
    def find(self, email:str) -> User:
        user_list = self.get_all()
        user_filtered: list = list(
            filter(lambda user: user if user.email == email else None, user_list)
        )
        if len(user_filtered) == 0:
            return None

        return user_filtered[0]

    def __initialize(self) -> None:
        if not os.path.exists(self._name):
            self.__save_list([])

    def __save_list(self, user_list: list[User]) -> None:
        with open(self._name, "wb") as file:
            pickle.dump(user_list, file)
