import pytest
import requests

from lib.Assertions import Assertions


class TestUserAgent():
    user_agent_values = {
        "user_agent": ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
                       "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        "user_agent1": ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                        "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        "user_agent2": ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        "user_agent3": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                        "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        "user_agent4": ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15"
                        "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    }
    expected_value = {
        "expected_value": {
            "platform": "Mobile",
            "browser": "No",
            "device": "Android"},
        "expected_value1": {
            "platform": "Mobile",
            "browser": "Chrome",
            "device": "iOS"},
        "expected_value2": {
            "platform": "Googlebot",
            "browser": "Unknown",
            "device": "Unknown"},
        "expected_value3": {
            "platform": "Web",
            "browser": "Chrome",
            "device": "No"},
        "expected_value4": {
            "platform": "Mobile",
            "browser": "No",
            "device": "iPhone"}
    }

    expected_results = [
        (user_agent_values["user_agent"],
         expected_value["expected_value"]["platform"],
         expected_value["expected_value"]["browser"],
         expected_value["expected_value"]["device"]),
        (user_agent_values["user_agent1"],
         expected_value["expected_value1"]["platform"],
         expected_value["expected_value1"]["browser"],
         expected_value["expected_value1"]["device"]),
        (user_agent_values["user_agent2"],
         expected_value["expected_value2"]["platform"],
         expected_value["expected_value2"]["browser"],
         expected_value["expected_value2"]["device"]),
        (user_agent_values["user_agent3"],
         expected_value["expected_value3"]["platform"],
         expected_value["expected_value3"]["browser"],
         expected_value["expected_value3"]["device"]),
        (user_agent_values["user_agent4"],
         expected_value["expected_value4"]["platform"],
         expected_value["expected_value4"]["browser"],
         expected_value["expected_value4"]["device"])]

    @pytest.mark.parametrize("user_agent,platform,browser,device", expected_results)
    def test_user_agent(self, user_agent, platform, browser, device):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={"User_agent": user_agent})
        print(dict(response.json()))
        actual_platform = response.json()["platform"]
        actual_browser = response.json()["browser"]
        actual_device = response.json()["device"]

        Assertions.assert_json_has_keys(response, [user_agent, platform, browser, device])