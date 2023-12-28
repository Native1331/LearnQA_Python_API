import requests
from lib import Assertions
from lib.base_case import BaseCase


class TestCookie(BaseCase):
    def test_cookie(self):
        main_url = "https://playground.learnqa.ru/api/get_auth_cookie"
        main_url1 = "https://playground.learnqa.ru/api/check_auth_cookie"
        payload = {"login": "secret_login", "password": "secret_pass"}
        response = requests.post(main_url, data = payload)
        print(response.cookies)
        if payload['login'] is not None:
            self.auth_cookie = self.get_cookie(response, "auth_cookie")
            cookies = {}
        if self.auth_cookie is not None:
            cookies.update({'auth_cookie': self.auth_cookie})

        response1 = requests.post(main_url1, data = cookies)
        print(response1.text)
        print(response1.cookies)

        Assertions.Assertions.assert_json_value_by_name(
            response1,
            "auth_cookie",
            cookies,
            "Auth cookie from auth method is not equal to Auth cookie from check method")
