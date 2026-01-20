"""
Problem: Set Practice
URL: https://neetcode.io/problems/python-set-practice/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List

def contains_duplicate(words: List[str]) -> bool:def contains_duplicate(words: List[str]) -> bool:
    convert_set=set(words)    convert_set=set(words)
    set_length=0    set_length=0
    for element in convert_set:    for element in convert_set:
        set_length+=1        set_length+=1
    if set_length!=len(words):    if set_length!=len(words):
        return True        return True
    else:    else:
        return False        return False

# do not modify code below this line# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))print(contains_duplicate(["hello", "world", "i", "am", "great"]))