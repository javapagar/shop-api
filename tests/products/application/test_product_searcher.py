import pytest
import os

from src.products.application.product_searcher import ProductSearcher
from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)
from tests.products.domain.product_builder import ProductBuilder


@pytest.fixture(autouse=True)
def create_repo():
    repo = InFileProductRepository("test.pkl")
    yield repo
    os.remove("test.pkl")


def test_product_searcher(create_repo, product_name, product_quantity, product_price):
    product = ProductBuilder().build()
    create_repo.save(product)
    searcher = ProductSearcher(create_repo)

    product_finded_dict = searcher.search(product.uuid)

    assert product_finded_dict.get("uuid") == product.uuid
