from api.domain.user_requet import UserRequest


class UserResponse(UserRequest):
    shopping_cart_uuid: str
