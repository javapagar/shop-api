from typing import Any

from src.shopping_cart.domain.product_repository import ProductRepository


class ShoppingCartRetriever:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def retrieve_all(self) -> list[dict[str,Any]]:
        product_list = self.repository.get_all()
        return product_list
