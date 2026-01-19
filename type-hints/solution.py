"""
Problem: Type Hints
URL: https://neetcode.io/problems/python-type-hints/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def greet(name: str) -> None:
    print("Hello, " + name)

value= greet("NeetCode")
print(type(value))