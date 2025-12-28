from uuid import uuid4
from src.shopping_cart.application.shopping_cart_saver import ShopingCartSaver


def test_product_saver(
    repo_cart, user_shopping_cart_id, product_name, product_quantity, product_price
):
    saver = ShopingCartSaver(repo_cart)
    uuid_product = uuid4().hex

    uuid_product_saved = saver.save(
        shopping_cart_uuid=user_shopping_cart_id,
        product_uuid=uuid_product,
        name=product_name,
        quantity=product_quantity,
        price=product_price,
    )

    product = repo_cart.get_product_by_id(user_shopping_cart_id, uuid_product_saved)
    assert uuid_product_saved == product.uuid
