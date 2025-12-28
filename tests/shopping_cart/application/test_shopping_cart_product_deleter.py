from tests.products.domain.product_builder import ProductBuilder
from src.shopping_cart.application.shopping_cart_product_deleter import (
    ShoppingCartProductDeleter,
)


def test_delete_product_with_one_item_from_cart(repo_cart, user_shopping_cart_id):
    deleter = ShoppingCartProductDeleter(repo_cart)
    product = ProductBuilder().with_quantity(1).build()
    product_id = product.uuid

    repo_cart.save_product(user_shopping_cart_id, product)
    product_id_deleted = deleter.delete(user_shopping_cart_id, product_id)
    product_checked = repo_cart.get_product_by_id(
        user_shopping_cart_id, product_id_deleted
    )

    assert product_id_deleted == product_id
    assert product_checked is None


def test_decrease_product_items_from_cart(repo_cart, user_shopping_cart_id):
    quantity = 3
    deleter = ShoppingCartProductDeleter(repo_cart)
    product = ProductBuilder().with_quantity(quantity).build()
    product_id = product.uuid

    repo_cart.save_product(user_shopping_cart_id, product)
    product_id_deleted = deleter.delete(user_shopping_cart_id, product_id)
    product_checked = repo_cart.get_product_by_id(
        user_shopping_cart_id, product_id_deleted
    )

    assert product_id_deleted == product_id
    assert product_checked.quantity == quantity -1 
