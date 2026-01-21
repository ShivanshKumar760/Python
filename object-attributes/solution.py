"""
Problem: Object Attributes
URL: https://neetcode.io/problems/python-object-attributes/question
Language: python

Solution by NeetCode GitHub Pusher
"""

# TODO: Print Whiskers' initial attributes
print(f"Intial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2
whiskers.hunger-=3
whiskers.energy+=2

# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

whiskers = Pet("Whiskers", "cat", 6, 8)

        self.hunger = hunger
        self.energy = energy
        self.species = species
        self.name = name
    def __init__(self, name: str, species: str, hunger: int, energy: int):
class Pet: