import requests

def test_headers():
  response = requests.get("https://playground.learnqa.ru/api/homework_header")
  expected_result = 'Some secret value'
  actual_result = response.headers.get("x-secret-homework-header")
  assert actual_result == expected_result, f"The headers are not match"

