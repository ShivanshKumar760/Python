"""
Problem: Abstraction
URL: https://neetcode.io/problems/python-abstraction/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Superhero:
    def __init__(self, name: str):
       self._name = name
       self._power_level = 40


# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  
    def fly(self):
        if(self.power>20):
            self.power-=20
            return "Up up and away!"
        elif(self.power<20):
            return "Too tired to fly..."
