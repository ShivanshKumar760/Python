"""
Problem: Self Parameter
URL: https://neetcode.io/problems/python-self-parameter/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class SuperHero:
    def __init__(self, name: str, power: str, strength: int):
        self.name = name
        self.power = power
        self.strength = strength

    def power_boost(self,additionalPow) -> None:
        self.strength += strength_increase
        print(f"{self.name}'s strength increased to {self.strength}!")



# Don't modify the following code
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

ironman.power_boost(15)
