"""
Problem: Implement Superhero Class
URL: https://neetcode.io/problems/python-implement-superhero-class/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name=name
        self.power=power
        self.health=health


# TODO: Create Superhero instances
batman=SuperHero("Batman","Intelligence",100)
superman=SuperHero("Superman","Strength",150)
# TODO: Print out the attributes of each superhero
print(batman.name)
print(batman.power)
print(batman.health)
print(superman.name)
print(superman.power)
print(superman.health)
