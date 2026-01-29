"""
Problem: Multiple Inheritance
URL: https://neetcode.io/problems/python-multiple-inheritance/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class ElectronicDevice:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def turn_on(self) -> None:
        print("Device is turning on")

    def turn_off(self) -> None:
        print("Device is turning off")

class HealthDevice:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def measure_heart_rate(self) -> None:
        print("Measuring heart rate")

