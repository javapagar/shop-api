from uuid import uuid4

from src.products.domain.product import Product
from src.products.domain.product_repository import ProductRepository


class ProductSaver:
    def __init__(self, saver: ProductRepository):
        self.saver = saver

    def save(self, name: str, quantity: int, price: float) -> str:
        uuid = uuid4().hex
        product = Product(uuid=uuid, name=name, quantity=quantity, price=price)
        self.saver.save(product)
        return uuid
