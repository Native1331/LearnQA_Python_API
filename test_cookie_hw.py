import requests

class TestOfCookie:
    def test_cookie():
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_value = (dict(response.cookies))
        actual_text = {'HomeWork': 'hw_value'}
        assert cookie_value == actual_text, f"This is not a cookie"





