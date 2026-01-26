"""
Problem: Static Methods
URL: https://neetcode.io/problems/python-static-methods/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`



print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
    @staticmethod
    def to_usd(ammount:int,currency:str):
        return ammount*CurrencyConverter.rates[currency]
