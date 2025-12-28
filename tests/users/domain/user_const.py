from random import randrange
from uuid import uuid4

from faker import Faker

faker = Faker()

USER_ID = uuid4().hex
USER_EMAIL = faker.email()
USER_PASSWORD = faker.password()
USER_ENABLE = randrange(0,1) == 1
USER_SHOPPING_CART_ID = uuid4().hex