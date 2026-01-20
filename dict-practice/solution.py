"""
Problem: Dict Practice
URL: https://neetcode.io/problems/python-dict-practice/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Dict # this adds type hinting for Dictfrom typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:def count_characters(word: str) -> Dict[str, int]:
    count=0    count=0
    rDict={}    rDict={}
    for i in word:    for i in word:
        for j in word:        for j in word:
            if i==j:            if i==j:
                count+=1                count+=1
                rDict[i]=count                rDict[i]=count
            else:            else:
                continue                continue
        count=0        count=0
    return rDict    return rDict





# don't modify below this line# don't modify below this line
print(count_characters("hello"))print(count_characters("hello"))
print(count_characters("world"))print(count_characters("world"))
print(count_characters("hello world"))print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))print(count_characters("this is a longer sentence"))
