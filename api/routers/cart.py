from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from api.application.product_cart_controller import ProductCartController
from api.application.login_cotroller import LoginCotroller

from api.domain.authenticator import OAUTH2_SCHEME
from api.domain.shopping_cart_product_request_reduced import ShoppingCartProductRequest
from api.domain.shopping_cart_product_list_response import (
    ShoppingCartProductListResponse,
)
from api.domain.product_response import ProductResponse
from api.domain.tags import Tags


router = APIRouter(
    prefix="/cart",
    tags=[Tags.SHOPPING_CART],
)

controller = ProductCartController()
login_controller = LoginCotroller()


async def check_authorize_to_cart(user_cart_id: str, token: str):
    user_authenticated = login_controller.decode_user(token)
    if (
        user_authenticated.shopping_cart_uuid is None
        or user_authenticated.shopping_cart_uuid != user_cart_id
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorize for this action",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get(
    "/{user_cart_id}",
    response_model=ShoppingCartProductListResponse,
    name="Get shopping cart",
    description="Return all products in shopping cart",
)
async def get_shopping_cart(
    user_cart_id: str, token: Annotated[str, Depends(OAUTH2_SCHEME)]
):
    await check_authorize_to_cart(user_cart_id, token)

    return controller.get_product_cart(user_cart_id)


@router.post(
    "/product",
    name="Save product",
    description="Save a product in de shopping cart",
    status_code=status.HTTP_201_CREATED,
)
async def save_product_cart(
    shopping_product_request: ShoppingCartProductRequest,
    token: Annotated[str, Depends(OAUTH2_SCHEME)],
):
    await check_authorize_to_cart(
        shopping_product_request.shopping_cart_uuid.root, token
    )
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
async def get_cart_product(
    cart_uuid: str, product_uuid: str, token: Annotated[str, Depends(OAUTH2_SCHEME)]
):
    await check_authorize_to_cart(cart_uuid, token)

    product = controller.search_product_in_cart(product_uuid, cart_uuid)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_uuid} not found",
        )
    return product


@router.delete(
    "", name="Delete product", description="Delete a product from a shopping cart"
)
async def delete_product(
    shopping_product_request: ShoppingCartProductRequest,
    token: Annotated[str, Depends(OAUTH2_SCHEME)],
):
    await check_authorize_to_cart(
        shopping_product_request.shopping_cart_uuid.root, token
    )
    return controller.delete_product_from_cart(
        shopping_product_request.product_uuid.root,
        shopping_product_request.shopping_cart_uuid.root,
    )
