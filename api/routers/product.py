import os
from fastapi import APIRouter, status

from api.domain.product_request import ProductRequest
from api.domain.tags import Tags
from api.domain.uuid_value import UUIDValue

from src.products.application.product_saver import ProductSaver
from src.products.application.product_list_retriever import ProductListRetriever
from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)

router = APIRouter(prefix="/product", tags=[Tags.PRODUCT])

path_product_data_file_name = os.getenv("PATH_PRODUCT", "./data/product.pkl")
product_repository = InFileProductRepository(path_product_data_file_name)


@router.get("")
async def get_product_list():
    product_list_retriever = ProductListRetriever(product_repository)
    return product_list_retriever.retrieve_all()


@router.post("", response_model=UUIDValue, status_code=status.HTTP_201_CREATED)
async def create_product(request: ProductRequest):
    product_saver = ProductSaver(product_repository)

    uuid_product_created = product_saver.save(
        name=request.name, quantity=request.quantity, price=request.price
    )

    return UUIDValue(uuid=uuid_product_created)
