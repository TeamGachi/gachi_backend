import os
from dotenv import load_dotenv

load_dotenv()

ENV = {
    "SECRETKEY" : os.getenv("SECRETKEY")
}

KAKAO = {
    "REST_API_KEY" : os.getenv("KAKAO_REST_API_KEY"),
    "KAKAO_REDIRECT_URI" : os.getenv("KAKAO_REDIRECT_URI"),
    "KAKAO_CLIENT_SECRET_KEY" : os.getenv("KAKAO_CLIENT_SECRET_KEY"),
    "KAKAO_LOGIN_URI" :  os.getenv("KAKAO_LOGIN_URI")
}