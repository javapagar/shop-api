from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart import ShoppingCart
from tests.users.domain.user_const import USER_ID


class ShoppingCartBuilder:
    def __init__(self):
        self._cart_uuid = USER_ID
        self._content = []

    def with_content(self, content: list[Product]) -> "ShoppingCartBuilder":
        self._content = content
        return self

    def with_cart_uuid(self, cart_uuid: str) -> "ShoppingCartBuilder":
        self._cart_uuid = cart_uuid
        return self

    def build(self) -> ShoppingCart:
        return ShoppingCart(
            content=self._content,
            cart_uuid=self._cart_uuid,
        )
