import os
import pickle
from typing import Optional

from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository
from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart import ShoppingCart


class InFileShoppingCartRepository(ShoppingCartRepository):
    def __init__(self, name: str):
        self._name = name

    def save_product(self, shopping_cart_id: str, product: Product) -> None:
        shopping_cart = self.get_by_id(shopping_cart_id)
        product_list = shopping_cart.content.model_dump()
        product_list.append(product)
        updated_shopping_cart = ShoppingCart(
            content=product_list, cart_uuid=shopping_cart_id
        )

        self.__save_shoppin_cart(updated_shopping_cart)

    def get_product_by_id(
        self, shopping_cart_id: str, product_id: str
    ) -> Optional[Product]:
        shopping_cart = self.get_by_id(shopping_cart_id)
        product_list = shopping_cart.content.root
        product_filtered: list = list(
            filter(
                lambda product: product if product.uuid == product_id else None,
                product_list,
            )
        )
        if len(product_filtered) == 0:
            return None

        return product_filtered[0]

    def delete_by_id(self, shopping_cart_id: str) -> None:
        if os.path.exists(self.__get_pkl_data_file_name(shopping_cart_id)):
            os.remove(self.__get_pkl_data_file_name(shopping_cart_id))

    def __exist_or_initialize(self, shopping_cart_id: str) -> None:
        path_file = self.__get_pkl_data_file_name(shopping_cart_id)
        path_dir, _ = os.path.split(path_file)

        if os.path.exists(path_file):
            return None

        if path_dir and not os.path.exists(path_dir):
            os.makedirs(path_dir)

        new_shopping_cart = ShoppingCart(cart_uuid=shopping_cart_id)
        self.__save_shoppin_cart(new_shopping_cart)

    def __save_shoppin_cart(self, shopping_cart: ShoppingCart):
        with open(self.__get_pkl_data_file_name(shopping_cart.cart_uuid), "wb") as file:
            pickle.dump(shopping_cart, file)

    def get_by_id(self, shopping_cart_id: str) -> ShoppingCart:
        pkl_data_file_name = self.__get_pkl_data_file_name(shopping_cart_id)

        self.__exist_or_initialize(shopping_cart_id)

        with open(pkl_data_file_name, "rb") as file:
            shopping_cart = pickle.load(file)

        return shopping_cart

    def __get_pkl_data_file_name(self, shopping_cart_id: str):
        name_parts = []
        path_parts = os.path.split(self._name)

        if shopping_cart_id:
            name_parts.append(shopping_cart_id)

        name_parts.append(path_parts[1])
        union_name = "_".join(name_parts)
        if path_parts[0]:
            union_name = f"{path_parts[0]}/{union_name}"

        return union_name
