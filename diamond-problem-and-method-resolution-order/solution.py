"""
Problem: Diamond Problem and Method Resolution Order
URL: https://neetcode.io/problems/python-diamond-problem-and-method-resolution-order/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("B")

class C(A):
    def print_method(self) -> None:
        print("C")

# class D(C, B): 
#     pass


# Do not change the code below
d = D()
d.print_method()
class D(B,C):
    pass
# print(D.__mro__)
