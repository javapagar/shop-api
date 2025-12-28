import os

import pytest
from uuid import uuid4

from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)
from src.shopping_cart.infrastructure.in_file_shopping_cart_repository import (
    InFileShoppingCartRepository,
)
from src.users.infrastructure.in_file_user_repository import InFileUserRepository
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


@pytest.fixture(autouse=True)
def repo_user():
    test_uuid = uuid4().hex
    file_name = f"{test_uuid}.pkl"
    repo = InFileUserRepository(file_name)
    yield repo
    os.remove(file_name)


@pytest.fixture()
def repo_product():
    test_uuid = uuid4().hex
    file_name = f"{test_uuid}.pkl"
    repo = InFileProductRepository(file_name)
    yield repo
    os.remove(file_name)


@pytest.fixture()
def repo_cart(user_shopping_cart_id):
    repo = InFileShoppingCartRepository("data/test.pkl")
    yield repo
    repo.delete_by_id(user_shopping_cart_id)
