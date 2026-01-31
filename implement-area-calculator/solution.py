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
    def calculate(self,length:int,width=None):
        if(width==None):
            return round(math.pi*(length**2),2)
        elif(width!=None):
            return int(length)*int(width)




# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
