from fastapi import APIRouter, status

from api.domain.env_vars import PATH_PRODUCT
from api.domain.product_request import ProductRequest
from api.domain.tags import Tags
from api.domain.uuid_value import UUIDValue

from src.products.application.product_saver import ProductSaver
from src.products.application.product_list_retriever import ProductListRetriever
from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)

router = APIRouter(prefix="/product", tags=[Tags.PRODUCT])

product_repository = InFileProductRepository(PATH_PRODUCT)


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

    return UUIDValue(root=uuid_product_created)
