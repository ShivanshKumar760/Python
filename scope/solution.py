"""
Problem: Scope
URL: https://neetcode.io/problems/python-scope/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def add_one(n):
    n = n + 1
    print(n)   

n = 10

add_one(n)     # Output: 11

print(n)       # Output: 10
