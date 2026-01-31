"""
Problem: Abstract Method and Class
URL: https://neetcode.io/problems/python-abstract-method-and-class/question
Language: python

Solution by NeetCode GitHub Pusher
"""


class PaymentCard(ABC):
    def __init__(self, card_number: str, balance: float):
        self.card_number = card_number
        self.balance = balance

    # TODO: Implement the process_payment method


# TODO: Implement the DebitCard class


    @abstractmethod
    def process_payment(self,amount)->str:
        pass
class DebitCard(PaymentCard):
    def process_payment(self,amount)->str:
        if(self.balance>=amount):
from abc import ABC, abstractmethod
            self.balance-=amount
            return "Payment successful"
        else:
            return "Insufficient funds"
# TODO: Implement the CreditCard class