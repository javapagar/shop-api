
from api.domain.product_response import ProductResponse
from tests import product_const

class ProductResponseBuilder:
    def __init__(self):
        self._uuid = product_const.PRODUCT_ID
        self._name = product_const.PRODUCT_NAME
        self._quantity = product_const.PRODUCT_QUANTITY
        self._price = product_const.PRODUCT_PRICE

    def with_id(self, uuid: str) -> "ProductResponseBuilder":
        self._uuid = uuid
        return self

    def with_name(self, name: str) -> "ProductResponseBuilder":
        self._name = name
        return self

    def with_quantity(self, quantity: int) -> "ProductResponseBuilder":
        self._quantity = quantity
        return self

    def with_price(self, price: float) -> "ProductResponseBuilder":
        self._price = price
        return self

    def build(self) -> ProductResponse:
        return ProductResponse(
            uuid=self._uuid, name=self._name, quantity=self._quantity, price=self._price
        )
