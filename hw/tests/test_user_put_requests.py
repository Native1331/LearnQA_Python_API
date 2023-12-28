import requests
from datetime import datetime
from lib.base_case import BaseCase
from lib.Assertions import Assertions


class TestChangeUsers(BaseCase):

    def test_change_user_without_auth(self):
        # REGISTER
        register_data = self.prepare_registration_data(prepa)
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id = self.get_json_value(response1, 'id')
        # EDIT
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/{user_id}",
                                 data={"first_name": new_name})
        Assertions.assert_code_status(response3, 200)


    def test_change_email_adress_in_authorization_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        actual_email = response1.json()["email"]
        print(actual_email)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # EDIT
        new_email = "123example.ru"
        response3 = requests.put(f"https://playground.learnqa.ru/api/{user_id}",
                                 headers={"auth_sid": auth_sid},
                                 cookies={"x-csrf-token": token},
                                 data={"email": new_email}
                                 )
        Assertions.assert_code_status(response3, 200)
