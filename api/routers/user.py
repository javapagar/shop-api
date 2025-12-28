import os

from fastapi import APIRouter

from api.domain.tags import Tags
from api.domain.user_requet import UserRequest
from api.domain.user_response import UserResponse
from src.users.application.user_saver import UserSaver
from src.users.application.user_searcher import UserSearcher
from src.users.infrastructure.in_file_user_repository import InFileUserRepository

router = APIRouter(
    prefix= "/user",
    tags= [Tags.USER],
)

data_user_file_name = os.getenv("PATH_USER", "./data/user.pkl")
user_repository = InFileUserRepository(data_user_file_name)

@router.get("/{id}", response_model=UserResponse)
async def get_user(id:str):
    searcher = UserSearcher(user_repository=user_repository)

    user = searcher.search(id)

    return user

@router.post("")
async def save_user(user_request:UserRequest):
    saver = UserSaver(user_repository)
    user_uuid = saver.save(user_request.email, user_request.password)
    return user_uuid