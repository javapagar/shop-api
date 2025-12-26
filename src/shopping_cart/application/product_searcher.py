from typing import Any, Optional

from src.shopping_cart.domain.product import Product
from src.shopping_cart.domain.product_repository import ProductRepository


class ProductSearcher:
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def search(self, uuid: str) -> Optional[dict[str, Any]]:
        product: Product = self._repository.find(uuid)
        if product is None:
            return None
        return product.model_dump()
