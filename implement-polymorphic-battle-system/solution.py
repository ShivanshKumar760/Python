"""
Problem: Implement Polymorphic Battle System
URL: https://neetcode.io/problems/python-implement-polymorphic-battle-system/question
Language: python

Solution by NeetCode GitHub Pusher
"""

        self.name = name
        self.health = 100
        self.power = power

    def attack(self) -> int:
        return self.power

# TODO: Implement the Warrior and Mage classes
class Warrior(Hero):
    def attack(self):
        return self.power+10
class Mage(Hero):