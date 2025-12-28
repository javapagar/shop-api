from pydantic import RootModel
from api.domain.product_response import ProductResponse

class ShoppingCartProductListResponse(RootModel):
    root: list[ProductResponse]