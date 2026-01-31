"""
Problem: Interface
URL: https://neetcode.io/problems/python-interface/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from abc import ABC, abstractmethod

# TODO: Create a Superhero interface


class Superman(Superhero):
    def fly(self) -> str:
        return "Up, up and away!"

    def use_power(self) -> str:
        return "Using heat vision"

class WonderWoman(Superhero):
    def fly(self) -> str:
        return "Soaring through the clouds!"

    def use_power(self) -> str:
        return "Using lasso of truth"



# Don't modify the code below
class Superhero(ABC):
    @abstractmethod
    def fly(self)->str:
        pass
    def use_power(self)->str:
        pass
superman = Superman()