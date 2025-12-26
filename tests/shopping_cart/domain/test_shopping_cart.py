import pytest

from src.shopping_cart.domain.product import Product
from src.shopping_cart.domain.shopping_cart import ShoppingCart
from tests.shopping_cart.domain.product_builder import ProductBuilder


@pytest.mark.parametrize(
    "name,quantity,price", [("test-1", 1, 2.0), ("test-2", 2, 1)]
)
def test_shopping_cart_build(name, quantity, price):
    product:Product = ProductBuilder().with_name(name).with_quantity(quantity).with_price(price).build()
    cart = ShoppingCart(content=[product])

    for product in cart.content:
        assert product.name == name
        assert product.price == price
        assert product.quantity == quantity

def test_shopping_cart_can_be_void():
        void_cart = []
       
        cart = ShoppingCart(content=void_cart)
        assert cart.content == void_cart
        cart = ShoppingCart()
        assert cart.content == void_cart
   