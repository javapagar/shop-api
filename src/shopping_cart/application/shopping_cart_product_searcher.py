from typing import Any, Optional

from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository


class ShoppingCartProductSearcher:
    def __init__(self, repository: ShoppingCartRepository):
        self._repository = repository

    def search(self, shopping_cart_uuid:str, product_uuid: str) -> Optional[dict[str, Any]]:
        product: Product = self._repository.get_product_by_id(shopping_cart_uuid, product_uuid)
        if product is None:
            return None
        return product.model_dump()
