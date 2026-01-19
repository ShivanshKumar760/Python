"""
Problem: Global vs Local Scope
URL: https://neetcode.io/problems/python-global-vs-local/question
Language: python

Solution by NeetCode GitHub Pusher
"""

n = 100

def print_local_variable(num: int) -> None:
    print(num)

print_local_variable(n)

print(n)
