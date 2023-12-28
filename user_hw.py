from datetime import datetime
from lib import Assertions
import requests
import pytest


def setup(self):
    base_part = "learnqa"
    domain = "example.com"
    random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    self.email = f"{base_part}{random_part}@{domain}"

    self.main_url = "https://playground.learnqa.ru/api/user"
    self.data = {
        "password": "123",
        "username": "learnqa",
        "firstName": "learnqa",
        "lastName": "learnqa",
        "email": self.email
    }


def test(self):
    response = requests.post(self.main_url, data=self.data)
    print(response.cookies)
    auth_sid = self.get_cookie(response, "auth_sid")
    token = self.get_header(response, "x-csrf-token")
    user_id = self.get_json_value(response, "user_id")
    print(auth_sid)
    print(token)
    print(user_id)
    response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=self.data)
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }
    response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
    auth_sid1 = self.get_cookie(response1, "auth_sid")
    token1 = self.get_header(response1, "x-csrf-token")
    user_id1 = self.get_json_value(response1, "user_id")
    print(auth_sid1)
    print(token1)
    print(user_id1)
    response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                             headers={"x-csrf-token": token},
                             cookies={"auth_sid": auth_sid})
