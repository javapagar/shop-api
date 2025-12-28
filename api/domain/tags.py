from enum import Enum


class Tags(Enum):
    HEALTH = "Health"
    SHOPPING_CART = "Shopping Cart"
    USER = "Users"
    PRODUCT = "Products"


tags_info = [
    {"name": Tags.HEALTH, "description": "Service health"},
    {"name": Tags.USER, "description": "Users service"},
    {"name": Tags.PRODUCT, "description": "Products service"},
    {"name": Tags.SHOPPING_CART, "description": "Shopping cart service"},
]
