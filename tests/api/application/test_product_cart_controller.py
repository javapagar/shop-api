import pytest
from uuid import uuid4

from api.application.product_cart_controller import ProductCartController
from tests.products.domain.product_builder import ProductBuilder


def test_search_product_in_cart(repo_cart, user_shopping_cart_id):
    controller = ProductCartController(None, repo_cart)

    product = controller.search_product_in_cart("test", user_shopping_cart_id)

    assert product is None


def test_add_product(repo_product):
    controller = ProductCartController(repo_product, None)

    product = controller.search_product("test")

    assert product is None


def test_add_product_to_cart(repo_product, repo_cart, user_shopping_cart_id):
    controller = ProductCartController(repo_product, repo_cart)
    product = ProductBuilder().build()
    uuid_product = product.uuid
    repo_product.save(product)

    uuid_product_in_cart = controller.add_product_to_cart(
        uuid_product, user_shopping_cart_id
    )

    assert uuid_product == uuid_product_in_cart


def test_add_product_to_cart_retrieve_none_if_not_product_exist(
    repo_product, repo_cart, user_shopping_cart_id
):
    controller = ProductCartController(repo_product, repo_cart)
    product_cart_not_existed = uuid4().hex

    with pytest.raises(ValueError, match="exists"):
        controller.add_product_to_cart(
        user_shopping_cart_id, product_cart_not_existed
    )


@pytest.mark.parametrize(
        "quantity, expected",
        [(2,3), (1,2), (5,6)]
)
def test_increase_quantity(quantity, expected):
    product = ProductBuilder().with_quantity(quantity).build()
    product_dict = product.model_dump()
    controller = ProductCartController(None, None)

    product_dict = controller.increase_quantity(product_dict)

    assert product_dict.get("quantity") == expected

@pytest.mark.parametrize(
        "quantity, expected",
        [(2,1), (1,0), (5,4)]
)
def test_decrease_quantity(quantity, expected):
    product = ProductBuilder().with_quantity(quantity).build()
    product_dict = product.model_dump()
    controller = ProductCartController(None, None)

    product_dict = controller.decrease_quantity(product_dict)

    assert product_dict.get("quantity") == expected


def test_decrease_quantity_faill_when_not_stock():
    quantity = 0
    product = ProductBuilder().with_quantity(quantity).build()
    product_dict = product.model_dump()
    controller = ProductCartController(None, None)

    with pytest.raises(ValueError, match ="stock"):
        controller.decrease_quantity(product_dict)
