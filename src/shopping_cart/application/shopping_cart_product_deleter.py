from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository


class ShoppingCartProductDeleter:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self._cart_repository = shopping_cart_repository

    def delete(self, uuid_cart: str, uuid_product: str) -> str:
        self._cart_repository.delete_product_by_id(uuid_cart, uuid_product)
        return uuid_product
