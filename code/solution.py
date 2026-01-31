"""
Problem: Code
URL: https://neetcode.io/problems/python-implement-area-calculator/solution
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
    def calculate(self,length:int,width=None):
        if(width==None):
            return round(math.pi*(length**2))
        elif(width!=None):

            return int(length)*int(width)
