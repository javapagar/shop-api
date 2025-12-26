from fastapi import APIRouter, HTTPException, status

from api.domain.product_request import ProductRequest
from api.domain.product_response import ProductResponse
from api.domain.tags import Tags
from src.shopping_cart.domain.shopping_cart import ShoppingCart
from src.shopping_cart.application.product_saver import ProductSaver
from src.shopping_cart.application.product_searcher import ProductSearcher
from src.shopping_cart.application.shopping_cart_retriever import ShoppingCartRetriever
from src.shopping_cart.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)

router = APIRouter(
    prefix="/cart",
    tags=[Tags.SHOPPING_CART]
)

product_repository = InFileProductRepository()

@router.get(
    "",
    response_model=ShoppingCart,
    name="Get shopping cart",
    description="Return all products in shopping cart",
)
async def get_all():
    retriever = ShoppingCartRetriever(repository=product_repository)
    products = retriever.retrieve_all()
    return ShoppingCart(content=products)


@router.post(
    "",
    name="Save product",
    description="Save a product in de shopping cart",
    status_code=status.HTTP_201_CREATED,
)
async def save_product_cart(product: ProductRequest):
    saver = ProductSaver(product_repository)
    return saver.save(product.name, product.quantity, product.price)


@router.get(
    "/{uuid}",
    response_model=ProductResponse,
    responses={
        404: {
            "description": "Product not found",
            "content": {
                "application/json": {"example": {"detail": "Product asdad not found"}}
            },
        }
    },
    name="Get product",
    description="Find a product from the shopping cart by uuid",
)
async def get_cart_product(uuid: str):
    retriever = ProductSearcher(repository=product_repository)
    product = retriever.search(uuid)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {uuid} not found"
        )
    return product