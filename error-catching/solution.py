"""
Problem: Error Catching
URL: https://neetcode.io/problems/python-error-catching/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def divide_numbers(a: str, b: str) -> None:def divide_numbers(a: str, b: str) -> None:
    try:    try:



# do not modify below this line# do not modify below this line
divide_numbers("10", "2")divide_numbers("10", "2")
divide_numbers("12", "0")divide_numbers("12", "0")
divide_numbers("2", "not a number")divide_numbers("2", "not a number")
        print(int(a)/int(b))        print(int(a)/int(b))

    except Exception as error:    except Exception as error:
        print("An error occurred:",error)        print("An error occurred:",error)
