import pytest

from tests.users.domain import user_const

@pytest.fixture
def user_id() -> str:
    return user_const.USER_ID


@pytest.fixture
def user_name() -> str:
    return user_const.USER_EMAIL


@pytest.fixture
def user_password() -> str:
    return user_const.USER_PASSWORD


@pytest.fixture
def user_enable() -> bool:
    return user_const.USER_ENABLE