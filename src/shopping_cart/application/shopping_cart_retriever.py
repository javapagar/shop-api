from typing import Any, Optional

from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartRetriever:
    def __init__(self, repository: ShoppingCartRepository):
        self.repository = repository

    def retrieve_all(self, cart_uuid:Optional[str]=None) -> list[dict[str,Any]]:
        shopping_cart = self.repository.get_by_id(cart_uuid)

        return shopping_cart.content.model_dump()
