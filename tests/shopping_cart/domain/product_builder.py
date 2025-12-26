
from src.shopping_cart.domain.product import Product
from tests.shopping_cart.domain import product_const

class ProductBuilder:
    def __init__(self):
        self._uuid = product_const.PRODUCT_ID
        self._name = product_const.PRODUCT_NAME
        self._quantity = product_const.PRODUCT_QUANTITY
        self._price = product_const.PRODUCT_PRICE

    def with_id(self, uuid: str) -> "ProductBuilder":
        self._uuid = uuid
        return self

    def with_name(self, name: str) -> "ProductBuilder":
        self._name = name
        return self

    def with_quantity(self, quantity: int) -> "ProductBuilder":
        self._quantity = quantity
        return self

    def with_price(self, price: float) -> "ProductBuilder":
        self._price = price
        return self

    def build(self) -> Product:
        return Product(
            uuid=self._uuid, name=self._name, quantity=self._quantity, price=self._price
        )
