import os

from fastapi import APIRouter, HTTPException, status

from api.application.product_cart_controller import ProductCartController
from api.domain.shopping_cart_product_request_reduced import ShoppingCartProductRequest
from api.domain.shopping_cart_product_list_response import (
    ShoppingCartProductListResponse,
)
from api.domain.product_response import ProductResponse
from api.domain.tags import Tags
from api.domain.uuid_value import UUIDValue
from src.shopping_cart.application.shopping_cart_saver import ShopingCartSaver
from src.shopping_cart.application.shopping_cart_product_searcher import (
    ShoppingCartProductSearcher,
)
from src.shopping_cart.application.shopping_cart_retriever import ShoppingCartRetriever

from src.products.infrastructure.in_file_product_repository import (
    InFileProductRepository,
)
from src.shopping_cart.infrastructure.in_file_shopping_cart_repository import (
    InFileShoppingCartRepository,
)

router = APIRouter(prefix="/cart", tags=[Tags.SHOPPING_CART])

path_data_cart_file_name = os.getenv("PATH_USER_CART", "./data/cart.pkl")
cart_repository = InFileShoppingCartRepository(path_data_cart_file_name)

path_data_product_file_name = os.getenv("PATH_PRODUCT", "./data/product.pkl")
product_repository = InFileProductRepository(path_data_product_file_name)

controller = ProductCartController(product_repository, cart_repository)


@router.get(
    "/{user_cart_id}",
    response_model=ShoppingCartProductListResponse,
    name="Get shopping cart",
    description="Return all products in shopping cart",
)
async def get_all(user_cart_id: str):
    retriever = ShoppingCartRetriever(repository=cart_repository)
    products = retriever.retrieve_all(user_cart_id)
    return products


@router.post(
    "/product",
    name="Save product",
    description="Save a product in de shopping cart",
    status_code=status.HTTP_201_CREATED,
)
async def save_product_cart(shopping_product_request: ShoppingCartProductRequest):
    try:
        return controller.add_product_to_cart(
            shopping_product_request.product_uuid.root,
            shopping_product_request.shopping_cart_uuid.root,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

@router.get(
    "/{cart_uuid}/product/{product_uuid}",
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
async def get_cart_product(cart_uuid: str, product_uuid):
    retriever = ShoppingCartProductSearcher(repository=cart_repository)
    product = retriever.search(cart_uuid, product_uuid)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_uuid} not found",
        )
    return product


@router.delete(
    "", name="Delete product", description="Delete a product from a shopping cart"
)
async def delete_product(shopping_product_request: ShoppingCartProductRequest):
    return controller.delete_product_from_cart(
        shopping_product_request.product_uuid.root,
        shopping_product_request.shopping_cart_uuid.root,
    )
