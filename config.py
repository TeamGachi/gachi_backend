import os
from dotenv import load_dotenv

load_dotenv()


env = {
    "SECRETKEY" : os.getenv("SECRETKEY")
}