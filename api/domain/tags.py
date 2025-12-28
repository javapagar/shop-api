from enum import Enum


class Tags(Enum):
    HEALTH = "Health"
    SHOPPING_CART = "Shopping Cart"
    USER = "User"


tags_info = [
    {"name": Tags.HEALTH, "description": "Service health"},
    {"name": Tags.USER, "description": "Users service"},
    {"name": Tags.SHOPPING_CART, "description": "Shopping cart service"},
]
