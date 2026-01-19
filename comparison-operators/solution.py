"""
Problem: Comparison Operators
URL: https://neetcode.io/problems/python-comparison-operators/question
Language: python

Solution by NeetCode GitHub Pusher
"""

//gnsdnjgj
def check_equal(x, y) -> bool:
    if(x==y):
        return True
    else:
        return False

def check_not_equal(x, y) -> bool:
    if(x != y):
        return True
    else:
        return False

def check_less_than(x, y) -> bool:
    if(x < y):
        return True
    else:
        return False

def check_greater_than(x, y) -> bool:
    if(x>y):
        return True
    else:
        return False

def check_less_than_or_equal(x, y) -> bool:
    if(x<=y):
        return True
    else:
        return False
def check_greater_than_or_equal(x, y) -> bool:
    if(x>=y):
        return True
    else:
        return False


# Don't change below this line
print("2 is equal to 2:", check_equal(2, 2))
print("-2 is equal to 2:", check_equal(-2, 2))

print("-2 is not equal to 2:", check_not_equal(-2, 2))
print("2 is not equal to 2:", check_not_equal(2, 2))

print("2 is less than 3:", check_less_than(2, 3))
print("3 is less than 3:", check_less_than(3, 3))
