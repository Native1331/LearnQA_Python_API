from lib.Assertions import Assertions
from lib.base_case import BaseCase
from lib.my_request import MyRequests


class TestUserGetHw(BaseCase):

    def test_get_user_details_such_as_another_user(self):
        # REGISTER
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data = data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        email = data.get("email")
        first_name = data.get("first_name")
        password = data.get("password")
        user_id = self.get_json_value(response, 'id')

        data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=data1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email1 = data1.get("email")
        first_name1 = data1.get("first_name")
        password1 = data1.get("password")
        user_id1 = self.get_json_value(response, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        print(response2.text)
        Assertions.assert_code_status(response2,200)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth = self.get_json_value(response2, "user_id")
        #GET USER
        response3 = MyRequests.get(f"/user/2",
                                 headers = {"x-csrf-token": token},
                                 cookies = {"auth_sid": auth_sid})
        print(response3.text)
        expected_keys = ["password", "firstName", "lastName", "email"]
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_keys(response3, "expected_keys")