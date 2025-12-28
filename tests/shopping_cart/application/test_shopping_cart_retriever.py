import pytest
from random import randrange
from uuid import uuid4

from src.shopping_cart.application.shopping_cart_retriever import ShoppingCartRetriever
from src.shopping_cart.infrastructure.in_file_shopping_cart_repository import (
    InFileShoppingCartRepository,
)
from tests.products.domain.product_builder import ProductBuilder


@pytest.fixture()
def create_repo(user_shopping_cart_id):
    repo = InFileShoppingCartRepository("data/test.pkl")
    yield repo
    repo.delete_by_id(user_shopping_cart_id)

def test_shopping_cart_retriever(create_repo, user_shopping_cart_id):
    number_product_expected = randrange(1, 10)
 
    retriever = ShoppingCartRetriever(create_repo)

    for _ in range(number_product_expected):
        product_uuid = uuid4().hex
        product = ProductBuilder().with_id(product_uuid).build()
        create_repo.save_product(user_shopping_cart_id, product)

    result_list = retriever.retrieve_all(user_shopping_cart_id)

    assert len(result_list) == number_product_expected
