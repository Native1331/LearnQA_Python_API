from lib.base_case import BaseCase
from lib.Assertions import Assertions
from lib.my_request import MyRequests

class TestUserDelete(BaseCase):
    def test_delete_user_without_auth(self):
        # AUTH
        login_data = {
          'email': 'vinkotov@example.com',
          'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)
        print(response2.text)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth = self.get_json_value(response2, "user_id")

        # DELETE
        response3 = MyRequests.delete(f"/user/{user_id_from_auth}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3, 400)
    def test_delete_user(self):
        # REGISTER
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        email = data.get("email")
        password = data.get("password")

        # AUTH
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)
        print(response2.text)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth = self.get_json_value(response2, "user_id")

        #DELETE
        response3 = MyRequests.delete(f"/user/{user_id_from_auth}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3,200)

        #CHECK_USER_ID
        response4 = MyRequests.get(f"user/{user_id_from_auth}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response4, 404)

    def test_delete_user_when_ahother_user_is_authorized(self):
            # REGISTER
            data = self.prepare_registration_data()
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_key(response, "id")
            email = data.get("email")
            password = data.get("password")

            # AUTH
            login_data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response2 = MyRequests.post("/user/login", data=login_data)
            Assertions.assert_code_status(response2, 200)
            print(response2.text)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")
            user_id_from_auth = self.get_json_value(response2, "user_id")

            # DELETE
            response3 = MyRequests.delete(f"/user/{user_id_from_auth}")
            Assertions.assert_code_status(response3, 400)