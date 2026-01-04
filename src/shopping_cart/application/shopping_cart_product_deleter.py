from src.shopping_cart.domain.shopping_cart_repository import ShoppingCartRepository


class ShoppingCartProductDeleter:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self._cart_repository = shopping_cart_repository

    def delete(self, uuid_cart: str, uuid_product: str) -> str:
        product = self._cart_repository.get_product_by_id(uuid_cart, uuid_product)

        if product is not None:
            if product.quantity == 1:
                self._cart_repository.delete_product_by_id(uuid_cart, uuid_product)
            else:
                product.quantity -= 1
                self._cart_repository.save_product(uuid_cart, product)
        
        return uuid_product
