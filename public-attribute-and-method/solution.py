"""
Problem: Public Attribute and Method
URL: https://neetcode.io/problems/python-public-attribute-and-method/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class StoreItem:
    def __init__(self,name,price):
       # pass  # Add: name, price


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them


       self.name=name
       self.price=price
print(f"Item: {chips.name} - Price: ${chips.price}")
