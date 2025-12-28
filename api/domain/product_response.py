from typing import Optional

from api.domain.product_request import ProductRequest

class ProductResponse(ProductRequest):
    uuid: Optional[str] = None

    def increase_quantity(self):
        self.quantity += 1
