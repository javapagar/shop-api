import pytest
import os

from src.products.application.product_saver import ProductSaver
from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)


@pytest.fixture(autouse=True)
def create_repo():
    repo = InFileProductRepository("test.pkl")
    yield repo
    os.remove("test.pkl")



def test_product_saver(
    create_repo, product_name, product_quantity, product_price
):
    saver = ProductSaver(create_repo)

    uuid_product_saved = saver.save(
        name=product_name, quantity=product_quantity, price=product_price
    )

    product = create_repo.find(uuid_product_saved)
    assert uuid_product_saved == product.uuid
