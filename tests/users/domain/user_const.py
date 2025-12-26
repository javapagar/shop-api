from random import randrange
from uuid import uuid4

USER_ID = uuid4().hex
USER_EMAIL = "test product"
USER_PASSWORD = "test_password"
USER_ENABLE = randrange(0,1) == 1