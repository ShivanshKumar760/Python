"""
Problem: Getter and Setter Methods
URL: https://neetcode.io/problems/python-getter-and-setter-methods/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class BankAccount:
    def __init__(self, balance: int):
         # Add private balance

    # TODO: Add getter method for balance
    def get_balance()->int:
    # TODO: Add setter method for balance




# Don't modify the code below this line
account = BankAccount(1000)
         self.__balance=balance
        return self.__balance
    def set_balance(new_balance:int)->None:
        if(new_balance<0):
            print("Cannot set negative balance!")
        self.__balance=new_balance
print(account.get_balance())