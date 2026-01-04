from typing import Any

from api.domain.product_response import ProductResponse
from src.shopping_cart.application.shopping_cart_saver import ShopingCartSaver
from src.shopping_cart.application.shopping_cart_product_searcher import (
    ShoppingCartProductSearcher,
)
from src.shopping_cart.application.shopping_cart_product_deleter import ShoppingCartProductDeleter
from src.products.application.product_searcher import ProductSearcher


class ProductCartController:
    def __init__(self, product_repository, cart_repository):
        self._product_repository = product_repository
        self._cart_repository = cart_repository

    def add_product_to_cart(self, uuid_product: str, uuid_cart: str) -> str:
        product_dict =self.search_product(uuid_product)
        if product_dict is None:
            raise ValueError("Product %s not exists", uuid_product)
        
        product_dict = self.decrease_quantity(product_dict)

        product_in_cart = self.search_product_in_cart(uuid_product, uuid_cart)
        
        if product_in_cart is not None:
            product_to_cart = self.increase_quantity(product_in_cart)
        else:
            product_to_cart = product_dict
            product_to_cart.update({"quantity":1})

        product_to_cart = ProductResponse(**product_to_cart)

        return self.save_product_in_cart(uuid_cart, product_to_cart)


    def save_product_in_cart(self, uuid_cart:str, product:ProductResponse):
        cart_saver = ShopingCartSaver(self._cart_repository)
        return cart_saver.save(
            uuid_cart, product.uuid, product.name, product.quantity, product.price
        )
    

    def search_product_in_cart(
        self, uuid_product: str, uuid_cart: str
    ) -> dict[str, Any]:
        product_in_cart_searcher = ShoppingCartProductSearcher(self._cart_repository)

        return product_in_cart_searcher.search(uuid_cart, uuid_product)
    
    def search_product(self, uuid_product)-> dict[str, Any]:
        product_searcher = ProductSearcher(self._product_repository)
        return product_searcher.search(uuid_product)
    
    def increase_quantity(self, product_dict: dict[str, Any]) -> dict[str,Any]:
        product_dict_aux = product_dict.copy()
        field_name = "quantity"
        value = product_dict_aux.get(field_name)
        if value is not None:
            increase_quantity = product_dict_aux.get(field_name) + 1
            product_dict_aux.update({field_name: increase_quantity})
            return product_dict_aux
        
        raise Exception("Field '%s' not exist", field_name)
    
    def decrease_quantity(self, product_dict: dict[str, Any]) -> dict[str,Any]:
        product_dict_aux = product_dict.copy()
        field_name = "quantity"
        value = product_dict_aux.get(field_name)
        if value is not None:
            decrease_quantity = product_dict_aux.get(field_name) - 1
            if decrease_quantity >=0:
                product_dict_aux.update({field_name: decrease_quantity})
                return product_dict_aux
            raise ValueError("Product is out of stock")
        
        raise ValueError("Field '%s' not exist", field_name)
        
    def delete_product_from_cart(self, uuid_product: str, uuid_cart: str) -> str:
        
        deleter = ShoppingCartProductDeleter(self._cart_repository)
        deleter.delete(uuid_cart, uuid_product)

        return uuid_product