"""
Problem: Intro to Classes
URL: https://neetcode.io/problems/python-intro-to-classes/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Pet:




# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
    def __init__(self,name:str,species:str)->None:
        self.name=name
        self.species=species
    #constructor
