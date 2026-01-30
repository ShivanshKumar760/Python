"""
Problem: Implement Polymorphic Battle System
URL: https://neetcode.io/problems/python-implement-polymorphic-battle-system/question
Language: python

Solution by NeetCode GitHub Pusher
"""

        return self.power+10
class Mage(Hero):
    def __init__(self,name,power):
        super.__init__()
        self.health-=20
    def attack(self):
        return self.power+20
# TODO: Implement the battle function
def show_attack(hero):
    print(f"{hero.name} attack with {hero.attack} damage")
    def attack(self):