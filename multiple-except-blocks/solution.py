"""
Problem: Multiple Except Blocks
URL: https://neetcode.io/problems/python-multiple-except-blocks/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a)/int(b))
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")