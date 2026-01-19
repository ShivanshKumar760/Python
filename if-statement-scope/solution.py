"""
Problem: If Statement Scope
URL: https://neetcode.io/problems/python-if-scope/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def pay_bill(balance: int, bill: int) -> int:
    if(balance >= bill):
        balance = balance - bill
        return balance
    else:
        return balance

# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
