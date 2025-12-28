
from api.domain.product_request import ProductRequest
from tests import product_const

class ProductRequestBuilder:
    def __init__(self):
        self._name = product_const.PRODUCT_NAME
        self._quantity = product_const.PRODUCT_QUANTITY
        self._price = product_const.PRODUCT_PRICE

    def with_name(self, name: str) -> "ProductRequestBuilder":
        self._name = name
        return self

    def with_quantity(self, quantity: int) -> "ProductRequestBuilder":
        self._quantity = quantity
        return self

    def with_price(self, price: float) -> "ProductRequestBuilder":
        self._price = price
        return self

    def build(self) -> ProductRequest:
        return ProductRequest(
            name=self._name, quantity=self._quantity, price=self._price
        )
