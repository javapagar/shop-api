from src.shopping_cart.application.shopping_cart_product_searcher import (
    ShoppingCartProductSearcher,
)
from tests.products.domain.product_builder import ProductBuilder


def test_product_searcher(repo_cart, user_shopping_cart_id):
    product = ProductBuilder().build()

    repo_cart.save_product(user_shopping_cart_id, product)
    searcher = ShoppingCartProductSearcher(repo_cart)

    product_finded_dict = searcher.search(user_shopping_cart_id, product.uuid)

    assert product_finded_dict.get("uuid") == product.uuid
