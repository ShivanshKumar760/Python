"""
Problem: Implement Area Calculator
URL: https://neetcode.io/problems/python-implement-area-calculator/question
Language: python

Solution by NeetCode GitHub Pusher
"""

import math

class AreaCalc:
    # TODO: Implement calculate method
    # pass



# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
    def calculate(length,width=None):
        if(width==None):
            return round(math.pi*(l**2))
        else:

            return length*width
