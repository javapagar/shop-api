import pytest

from tests.shopping_cart.domain import product_const

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
