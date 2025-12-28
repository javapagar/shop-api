from abc import ABC, abstractmethod
from src.products.domain.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> None: ...

    @abstractmethod
    def get_all(self)-> list[Product]: ...

    @abstractmethod
    def find(self, id:str) -> Product: ...