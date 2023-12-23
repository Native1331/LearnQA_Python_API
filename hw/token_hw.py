import time
import requests

status1 = 'Job is NOT ready'
status2 = 'Job is ready'


response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token_value = response.json()['token']
time_value = response.json()['seconds']
data = {'token': token_value}
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = data)
print(response1.text)
status = response1.json()['status']

if status == status1:
    assert status == status1, "Job is NOT ready"
    time.sleep(time_value)
if status == status2:
    result = response1.json()['result']
    print(status,result)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = data)
print(response3.text)
final_status = response3.json()['status']
print(final_status)
assert final_status == status2, "Job is ready"





