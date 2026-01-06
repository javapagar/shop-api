from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm

from api.application.login_cotroller import LoginCotroller
from api.domain.tags import Tags

router = APIRouter(prefix="/token", tags=[Tags.SECURITY])
controller = LoginCotroller()


@router.post("")
async def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):

    user_dict = controller.login(form_data.username, form_data.password)

    if  user_dict is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = controller.create_access_token(user_dict.model_dump())
    return {"access_token": token, "token_type": "bearer"}