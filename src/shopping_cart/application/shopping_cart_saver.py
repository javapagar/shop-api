from uuid import uuid4

from src.products.domain.product import Product
from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository


class ShopingCartSaver:
    def __init__(self, saver: ShoppingCartRepository):
        self.saver = saver

    def save(self, shopping_cart_uuid:str, name: str, quantity: int, price: float) -> str:
        uuid = uuid4().hex
        product = Product(uuid=uuid, name=name, quantity=quantity, price=price)
        self.saver.save_product(shopping_cart_uuid, product)
        return uuid
