from random import randrange
from uuid import uuid4

from src.shopping_cart.application.shopping_cart_retriever import ShoppingCartRetriever
from tests.products.domain.product_builder import ProductBuilder


def test_shopping_cart_retriever(repo_cart, user_shopping_cart_id):
    number_product_expected = randrange(1, 10)

    retriever = ShoppingCartRetriever(repo_cart)

    for _ in range(number_product_expected):
        product_uuid = uuid4().hex
        product = ProductBuilder().with_id(product_uuid).build()
        repo_cart.save_product(user_shopping_cart_id, product)

    result_list = retriever.retrieve_all(user_shopping_cart_id)

    assert len(result_list) == number_product_expected
