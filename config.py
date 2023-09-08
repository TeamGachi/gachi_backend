import os
from dotenv import load_dotenv

load_dotenv()


ENV = {
    "SECRETKEY" : os.getenv("SECRETKEY")
}

KAKAO = {
    "REST_API_KEY" : os.getenv("KAKAO_REST_API_KEY"),
    "KAKAO_REDIRECT_URI" : os.getenv("KAKAO_REDIRECT_URI")
}