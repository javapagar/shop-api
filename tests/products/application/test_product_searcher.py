from src.products.application.product_searcher import ProductSearcher
from tests.products.domain.product_builder import ProductBuilder


def test_product_searcher(repo_product):
    product = ProductBuilder().build()
    repo_product.save(product)
    searcher = ProductSearcher(repo_product)

    product_finded_dict = searcher.search(product.uuid)

    assert product_finded_dict.get("uuid") == product.uuid
