from api.domain.product_response import ProductResponse
from tests.api.domain.product_response_builder import ProductResponseBuilder

def test_product_response_build(product_id, product_name, product_quantity, product_price):

    product: ProductResponse = ProductResponseBuilder().build()

    assert product.uuid == product_id
    assert product.name == product_name
    assert product.price == product_price
    assert product.quantity == product_quantity
