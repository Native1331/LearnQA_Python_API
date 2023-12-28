from lib.base_case import BaseCase
from lib.Assertions import Assertions
from lib.my_request import MyRequests
class TestChangeUsers(BaseCase):

    def test_change_user_without_auth(self):
        # REGISTER
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        user_id = self.get_json_value(response, 'id')

        # EDIT
        new_name = "Changed Name"
        response1 = MyRequests.put(f"/user/{user_id}",
                                    data = {"firstName": new_name})
        Assertions.assert_code_status(response1, 400)


    def test_change_email_adress_in_authorization_user(self):
        # REGISTER
        data = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        email = data.get("email")
        password = data.get("password")

        #AUTH
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response3,200)
        print(response3.text)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3,"x-csrf-token")
        user_id_from_auth = self.get_json_value(response3, "user_id")

         # EDIT
        new_email = "123example.ru"
        response2 = MyRequests.put(f"/user/{user_id_from_auth}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": new_email})
        Assertions.assert_code_status(response2, 400)
    def test_change_name_to_one_letter(self):
        # REGISTER
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        user_id = self.get_json_value(response, 'id')
        email = data.get("email")
        password = data.get("password")
        # AUTH
        login_data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        print(response1.text)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth = self.get_json_value(response1, "user_id")
        # EDIT
        new_name = "V"
        response2 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})

        Assertions.assert_code_status(response2, 400)