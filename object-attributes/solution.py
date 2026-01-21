"""
Problem: Object Attributes
URL: https://neetcode.io/problems/python-object-attributes/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(f"Intial Attribute: {whiskers.name}({whiskers.species})-Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes
whiskers.hunger-=1
whiskers.energy+=2
print(f"Modified Attribute: {whiskers.name}({whiskers.species})-Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")