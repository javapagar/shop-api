import pytest
from uuid import uuid4

from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart import ShoppingCart
from tests.products.domain.product_builder import ProductBuilder
from tests.shopping_cart.domain.shopping_cart_builder import ShoppingCartBuilder


@pytest.mark.parametrize("name,quantity,price", [("test-1", 1, 2.0), ("test-2", 2, 1)])
def test_shopping_cart_build(name, quantity, price):
    product: Product = (
        ProductBuilder()
        .with_name(name)
        .with_quantity(quantity)
        .with_price(price)
        .build()
    )
    cart_uuid = uuid4().hex
    cart = (
        ShoppingCartBuilder()
        .with_content(content=[product])
        .with_cart_uuid(cart_uuid)
        .build()
    )

    for product in cart.content.root:
        assert product.name == name
        assert product.price == price
        assert product.quantity == quantity

    assert cart.cart_uuid == cart_uuid


def test_shopping_cart_can_be_void():
    void_cart = []
    cart_uuid = uuid4().hex

    cart = ShoppingCartBuilder().with_content(content=void_cart).build()

    assert cart.content.model_dump() == void_cart

    cart = ShoppingCart(cart_uuid=cart_uuid)

    assert cart.content.model_dump() == void_cart
