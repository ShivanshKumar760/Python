"""
Problem: Try Except
URL: https://neetcode.io/problems/python-try-except/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def divide_numbers(a: int, b: int) -> None:def divide_numbers(a: int, b: int) -> None:
    try:    try:
        print(a/b)        print(a/b)
    except:    except:
        print("An error occurred!")        print("An error occurred!")



# do not modify below this line# do not modify below this line
divide_numbers(10, 2)divide_numbers(10, 2)
divide_numbers(12, 3)divide_numbers(12, 3)
divide_numbers(2, 0)divide_numbers(2, 0)
