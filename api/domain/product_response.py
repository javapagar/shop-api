from typing import Optional

from api.domain.product_request import ProductRequest

class ProductResponse(ProductRequest):
    uuid: Optional[str] = None
