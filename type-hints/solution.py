"""
Problem: Type Hints
URL: https://neetcode.io/problems/python-type-hints/question
Language: python

Solution by NeetCode GitHub Pusher
"""

# def greet(name: str) -> str:
#     # print("Hello, " + name)
def greet(name:str)->None:
value= greet("NeetCode")
#     return "Hello, "+name
    print("Hello, "+name)
    
print(type(value))