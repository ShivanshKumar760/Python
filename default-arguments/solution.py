"""
Problem: Default Arguments
URL: https://neetcode.io/problems/python-default-arguments/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def greet(name, punctuation="!") -> None:
    print("Hello, " + name + punctuation)

greet("World", "!")
greet("World")
