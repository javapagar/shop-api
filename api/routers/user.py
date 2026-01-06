import os
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from dotenv import load_dotenv

from api.application.login_cotroller import LoginCotroller
from api.application.users_cotroller import UsersController
from api.domain.authenticator import OAUTH2_SCHEME
from api.domain.tags import Tags
from api.domain.user_requet import UserRequest
from api.domain.user_response import UserResponse
from src.users.infrastructure.in_file_user_repository import InFileUserRepository


load_dotenv()

router = APIRouter(
    prefix="/user",
    tags=[Tags.USER],
)

oauth2_scheme = OAUTH2_SCHEME
user_controller = UsersController()
login_cotroller = LoginCotroller()


@router.get("/{email}", response_model=UserResponse)
async def get_user(email: str, token: Annotated[str, Depends(oauth2_scheme)]):
    user = user_controller.get_user_info(email)
    user_authenticated = login_cotroller.decode_user(token)

    if user_authenticated.email is None or user_authenticated.email != user.email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.post("")
async def register_user(user_request: UserRequest):
    user_uuid = user_controller.save_user(user_request.email, user_request.password)
    return user_uuid
