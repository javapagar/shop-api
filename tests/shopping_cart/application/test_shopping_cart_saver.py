import pytest

from src.shopping_cart.application.shopping_cart_saver import ShopingCartSaver
from src.shopping_cart.infrastructure.in_file_shopping_cart_repository import (
    InFileShoppingCartRepository,
)


@pytest.fixture()
def create_repo(user_shopping_cart_id):
    repo = InFileShoppingCartRepository("data/test.pkl")
    yield repo
    repo.delete_by_id(user_shopping_cart_id)


def test_product_saver(
    create_repo, user_shopping_cart_id, product_name, product_quantity, product_price
):
    saver = ShopingCartSaver(create_repo)

    uuid_product_saved = saver.save(
        shopping_cart_uuid=user_shopping_cart_id,
        name=product_name,
        quantity=product_quantity,
        price=product_price,
    )

    product = create_repo.get_product_by_id(user_shopping_cart_id, uuid_product_saved)
    assert uuid_product_saved == product.uuid
