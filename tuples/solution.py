"""
Problem: Tuples
URL: https://neetcode.io/problems/python-tuples/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Tuple # this is to add type hints for tuplesfrom typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:def create_pair(name: str, age: int) -> Tuple[str, int]:
    return (name,age)    return (name,age)

# do not modify code below this line# do not modify code below this line
print(create_pair("Alice", 25))print(create_pair("Alice", 25))
print(create_pair("Bob", 30))print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))print(create_pair("Charlie", 35))
