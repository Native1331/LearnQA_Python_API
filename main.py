import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params = payload)
print(response.text)
parsed_response_text = response.json()
print(parsed_response_text["answer"])

response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects = True)
first_response = response.history[0]
second_response = response
print(response.status_code)
print(first_response.url)
print(second_response.url)