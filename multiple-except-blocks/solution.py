"""
Problem: Multiple Except Blocks
URL: https://neetcode.io/problems/python-multiple-except-blocks/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def divide_numbers(a: str, b: str) -> None:def divide_numbers(a: str, b: str) -> None:
    try:    try:



        print(int(a)/int(b))        print(int(a)/int(b))
    except ValueError:    except ValueError:
# do not modify below this line# do not modify below this line
divide_numbers("10", "2")divide_numbers("10", "2")
divide_numbers("12", "0")divide_numbers("12", "0")
        print("Error: Invalid value!")        print("Error: Invalid value!")
    except ZeroDivisionError:    except ZeroDivisionError:
        print("Error: Division by zero!")        print("Error: Division by zero!")
    except Exception as error:    except Exception as error:
        print("An error occurred:", error)        print("An error occurred:", error)