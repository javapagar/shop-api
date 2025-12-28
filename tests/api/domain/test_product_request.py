from api.domain.product_request import ProductRequest
from tests.api.domain.product_request_builder import ProductRequestBuilder

def test_product_build(product_id, product_name, product_quantity, product_price):

    product: ProductRequest = ProductRequestBuilder().build()
    
    assert product.name == product_name
    assert product.price == product_price
    assert product.quantity == product_quantity
