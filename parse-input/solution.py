"""
Problem: Parse Input
URL: https://neetcode.io/problems/python-parse-input/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List

def read_integers() -> List[int]:def read_integers() -> List[int]:
    container=input()    container=input()

    returnL=[]    returnL=[]
    for i in range (len(container.split(","))):    for i in range (len(container.split(","))):
        returnL.append(int(container.split(",")[i]))        returnL.append(int(container.split(",")[i]))
    return returnL    return returnL
                

# do not modify the code below# do not modify the code below
print(read_integers())print(read_integers())
print(read_integers())print(read_integers())
print(read_integers())print(read_integers())