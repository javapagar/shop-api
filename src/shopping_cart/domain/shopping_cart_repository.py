from abc import ABC, abstractmethod

from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart import ShoppingCart


class ShoppingCartRepository(ABC):
    @abstractmethod
    def save_product(self, shopping_cart_id: str, product: Product) -> None: ...

    @abstractmethod
    def get_by_id(self, shopping_cart_id: str) -> ShoppingCart: ...

    @abstractmethod
    def get_product_by_id(self, shopping_cart_id: str, product_id: str) -> Product: ...

    @abstractmethod
    def delete_by_id(self, shopping_cart_id: str) -> None: ...

    @abstractmethod
    def delete_product_by_id(self, shopping_cart_id: str, product_id: str) -> None: ...
