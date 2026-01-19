"""
Problem: If Statements
URL: https://neetcode.io/problems/python-if/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def is_balance_low(balance: int) -> None:
    if(balance<=100):
        print("Warning: Low balance.")
# do not modify below this line
is_balance_low(99)
is_balance_low(100)
is_balance_low(101)
