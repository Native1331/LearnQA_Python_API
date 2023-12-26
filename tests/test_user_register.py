import requests
import pytest
from lib.base_case import BaseCase
from lib.Assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

        self.main_url =  "https://playground.learnqa.ru/api/user"
        self.data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
        }

    def test_create_user_succesfully(self):
        response = requests.post(self.main_url, data= self.data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
        response = requests.post(self.main_url, data = data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content{response.content}"
    def test_create_user_with_wrong_email(self):
        email = 'vinkotovexample.com'
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
        response = requests.post(self.main_url, data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content{response.content}"

    data = [
        ("'username': 'learnqa','firstName': 'learnqa','lastName': 'learnqa','email': self.email"),
        ("'password': '123', 'firstName': 'learnqa','lastName': 'learnqa','email': self.email"),
        ("'password': '123', 'username': 'learnqa','lastName': 'learnqa','email': self.email"),
        ("'password': '123', 'username': 'learnqa','firstName': 'learnqa','email': self.email"),
        ("'password': '123', 'username': 'learnqa','firstName': 'learnqa','lastName': 'learnqa'"),
    ]
    @pytest.mark.parametrize('data', data)
    def test_created_user_without_field(self, data):
        response = requests.post(self.main_url, data = data)
        Assertions.assert_code_status(response, 400)
        print(response.text)
        print(response.content)
        assert response.content.decode("utf-8") == (f"The following required params are missed: email, "
                                                    f"password, username, firstName, lastName"), \
            f"Unexpected response content{response.content}"

    def test_created_user_with_short_name(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "l",
            "lastName": "learnqa",
            "email": self.email}
        response = requests.post(self.main_url, data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short", \
            f"Unexpected response content{response.content}"
    def test_created_user_with_long_name(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaart"
                         "learnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaart"
                         "learnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartlearnqaartl",
            "lastName": "learnqa",
            "email": self.email}
        response = requests.post(self.main_url, data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", \
            f"Unexpected response content{response.content}"






