import os
import pickle
from typing import Optional

from src.products.domain.product_repository import ProductRepository
from src.products.domain.product import Product


class InFileProductRepository(ProductRepository):
    def __init__(self, name:str):
        self._name = name
        self.__initialize()

    def save(self, product: Product) -> None:
        product_list: list[Product] = self.get_all()
        product_list.append(product)
        self.__save_list(product_list)

    def get_all(self) -> list[Product]:
        with open(self._name, "rb") as file:
            product_list = pickle.load(file)
        return product_list

    def find(self, id) -> Optional[Product]:
        product_list = self.get_all()
        product_filtered:list = list(
            filter(
                lambda product: product if product.uuid == id else None, product_list
            )
        )
        if len(product_filtered) == 0:
            return None
        
        return product_filtered[0]

    def __initialize(self):
        if not os.path.exists(self._name):
            self.__save_list([])

    def __save_list(self, product_list: list[Product]):
        with open(self._name, "wb") as file:
            pickle.dump(product_list, file)
