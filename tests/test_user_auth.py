import pytest
import requests
from lib.base_case import BaseCase
from lib.Assertions import Assertions
import allure

from lib.my_request import MyRequests


@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    @allure.description("This test succesfully authorize user by email and password")
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data = data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User Id from auth method is not equal to user Id from check method"
        )

        exclude_params = [
            ("no_cookie"),
            ("no_token")
        ]

        @allure.description("This test checks authorization status without sending auth cookie or token")
        @pytest.mark.parametrize('condition', exclude_params)
        def test_negative_auth_check(self, condition):
            data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }

            response1 = MyRequests.post("/user/login", data=data)

            self.auth_sid = self.get_cookie(response1, "auth_sid")
            self.token = self.get_header(response1, "x-csrf-token")
            self.user_id_from_auth_method = self.get_json(response1, "user_id")

            auth_sid = response1.cookies.get("auth_sid")
            token = response1.cookies.get("x-csrf-token")
            if condition == "no cookie":
                response2 = MyRequests.get("/user/auth")
                headers = {"x-csrf-token": token}
            else:
                response2 = MyRequests.get("/user/auth")
                cookies = {"auth_sid": auth_sid}

                assert "user_id" in response2.json(), "There is no userId in the second response"
                user_id_from_check_method = response2.json()["user_id"]
                assert user_id_from_check_method == 0, f"User is authorized condition {condition}"
