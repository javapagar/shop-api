import pytest

from src.shopping_cart.application.shopping_cart_product_searcher import ShoppingCartProductSearcher
from src.shopping_cart.infrastructure.in_file_shopping_cart_repository import (
    InFileShoppingCartRepository,
)
from tests.products.domain.product_builder import ProductBuilder

@pytest.fixture()
def create_repo(user_shopping_cart_id):
    repo = InFileShoppingCartRepository("data/test.pkl")
    yield repo
    repo.delete_by_id(user_shopping_cart_id)

def test_product_searcher(create_repo, user_shopping_cart_id):
    product = ProductBuilder().build()

    create_repo.save_product(user_shopping_cart_id, product)
    searcher = ShoppingCartProductSearcher(create_repo)

    product_finded_dict = searcher.search(user_shopping_cart_id, product.uuid)

    assert product_finded_dict.get("uuid") == product.uuid
