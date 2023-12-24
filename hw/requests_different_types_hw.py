import requests
methods = ["GET","POST","PUT","DELETE"]
main_url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
response = requests.get(main_url)
first_response = requests.post(main_url)
second_response = requests.put(main_url)
third_response = requests.delete(main_url)

fourth_response = requests.head(main_url)

print(first_response.text)
print(fourth_response.text)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for method in methods:
    get_response = requests.get(main_url, params={'method': f"{method}"})
    print(f"GET request with parameter 'method' : {method}")
    print(f"Response code: {get_response.status_code}")
    print(f"Response text: {get_response.text}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    post_response = requests.post(main_url, data={'method': f"{method}"})
    print(f"POST request with parameter 'method' : {method}")
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    put_response = requests.put(main_url, data={'method': f"{method}"})
    print(f"PUT request with parameter 'method' : {method}")
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    delete_response = requests.delete(main_url, data={'method': f"{method}"})
    print(f"DELETE request with parameter 'method' : {method}")
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



