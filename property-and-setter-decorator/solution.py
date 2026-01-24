"""
Problem: Property and Setter Decorator
URL: https://neetcode.io/problems/python-property-and-setter-decorator/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class BankAccount:
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line
    def balance(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.__balance

    @balance.setter
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
    @property       
    def balance(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
