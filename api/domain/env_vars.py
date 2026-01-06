from dotenv import load_dotenv
import os

load_dotenv()

PATH_PRODUCT = os.getenv("PATH_PRODUCT")
PATH_USER_CART = os.getenv("PATH_USER_CART")
PATH_USER = os.getenv("PATH_USER")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
