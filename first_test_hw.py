import requests
import pytest


class TestFirst:
    def test_string_wih_15_letters(self):
        phrase = input("Set a phrase: ")
        expected_text = {}
        if len(phrase) >= 15:
            expected_text = phrase
        else:
            expected_text = f"This string {phrase} has more than 15 letters"

        assert phrase == expected_text, f"This string {phrase} has more than 15 letters"
