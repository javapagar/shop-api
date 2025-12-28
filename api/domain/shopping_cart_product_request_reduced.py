from pydantic import BaseModel

from api.domain.uuid_value import UUIDValue


class ShoppingCartProductRequest(BaseModel):
    shopping_cart_uuid: UUIDValue
    product_uuid: UUIDValue
