"""
Problem: Getter and Setter Methods
URL: https://neetcode.io/problems/python-getter-and-setter-methods/question
Language: python

Solution by NeetCode GitHub Pusher
"""

    def get_balance(self)->int:
    # TODO: Add setter method for balance




# Don't modify the code below this line
account = BankAccount(1000)
        return self.__balance
    def set_balance(new_balance:int)->None:
        if(new_balance<0):
            print("Cannot set negative balance!")
        self.__balance=new_balance
print(account.get_balance())
    # TODO: Add getter method for balance

account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())