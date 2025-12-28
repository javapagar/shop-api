from random import randrange, uniform
from uuid import uuid4

PRODUCT_ID = uuid4().hex
PRODUCT_NAME = "test product"
PRODUCT_QUANTITY = randrange(1,10)
PRODUCT_PRICE = uniform(0.5, 300.0)