from src.products.domain.product import Product
from tests.products.domain.product_builder import ProductBuilder

def test_product_build(product_id, product_name, product_quantity, product_price):

    product: Product = ProductBuilder().build()

    assert product.uuid == product_id
    assert product.name == product_name
    assert product.price == product_price
    assert product.quantity == product_quantity
