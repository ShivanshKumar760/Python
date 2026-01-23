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