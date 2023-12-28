import requests


expected_value = {
    "expected_result": {
        "platform": "Mobile",
        "browser": "No",
        "device": "Android"},
    "expected_result_1": {
        "platform": "Mobile",
        "browser": "Chrome",
        "device": "iOS"},
    "expected_result_2": {
        "platform": "Googlebot",
        "browser": "Unknown",
        "device": "Unknown"},
    "expected_result_3": {
        "platform": "Web",
        "browser": "Chrome",
        "device": "No"},
    "expected_result_4": {
        "platform": "Mobile",
        "browser": "No",
        "device": "iPhone"}
}
expected_fields = [
    (user_agent_values["user_agent_1"],
     expected_value["expected_result"]["platform"],
     expected_value["expected_result"]["browser"],
     expected_value["expected_result"]["device"]),
    (user_agent_values["user_agent_2"],
     expected["exp_result_2"]["platform"],
     expected["exp_result_2"]["browser"],
     expected["exp_result_2"]["device"]),
    (user_agent_values["user_agent_3"],
     expected["exp_result_3"]["platform"],
     expected["exp_result_3"]["browser"],
     expected["exp_result_3"]["device"]),
    (user_agent_values["user_agent_4"],
     expected["exp_result_4"]["platform"],
     expected["exp_result_4"]["browser"],
     expected["exp_result_4"]["device"]),
    (user_agent_values["user_agent_5"],
     expected["exp_result_5"]["platform"],
     expected["exp_result_5"]["browser"],
     expected["exp_result_5"]["device"])
]
expected_fields = [( user_agent: user_agent_value,
                    platform: platform_value,
                    browser: browser_value;
                    device: device_value)]
e





response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                        headers={"User_agent": user_agent})
actual_platform = response.json()["platform"]
actual_browser = response.json()["browser"]
actual_device = response.json()["device"]

user_agent1 = response.json()
print(response.headers)
print(user_agent1)
print(response.text)
print(dict(response.json()))
