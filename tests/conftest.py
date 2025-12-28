import pytest

from tests import product_const
from tests.users.domain import user_const

@pytest.fixture
def product_id() -> str:
    return product_const.PRODUCT_ID


@pytest.fixture
def product_name() -> str:
    return product_const.PRODUCT_NAME


@pytest.fixture
def product_quantity() -> int:
    return product_const.PRODUCT_QUANTITY


@pytest.fixture
def product_price() -> float:
    return product_const.PRODUCT_PRICE


@pytest.fixture
def user_id() -> str:
    return user_const.USER_ID


@pytest.fixture
def user_email() -> str:
    return user_const.USER_EMAIL


@pytest.fixture
def user_password() -> str:
    return user_const.USER_PASSWORD


@pytest.fixture
def user_enable() -> bool:
    return user_const.USER_ENABLE

@pytest.fixture
def user_shopping_cart_id() -> str:
    return user_const.USER_SHOPPING_CART_ID
