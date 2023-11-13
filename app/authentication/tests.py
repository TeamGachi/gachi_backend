from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.views import status

# Create your tests here.


class LoginTestCase(APITestCase):
    def setUp(self):
        self.url_1 = "/api/authentication/login"
        self.data = {
            "email": "testemail@naver.com",
            "name": "turing",
            "gender": "남자",
            "birth": "1999-08-22",
        }

    def test_normal_signup_case(self):
        response = self.client.post(self.url_1, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anomaly_signup_case(self):
        data = {
            "email": "testemailnaver.com",
            "name": "turing",
            "gender": "남자",
            "birth": "1999-08-22",
        }

        response = self.client.post(self.url_1, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
