"""
Problem: Intro to Dictionaries
URL: https://neetcode.io/problems/python-intro-to-dictionaries/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List, Dictfrom typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:def create_dict(name: str, age: int) -> Dict[str, int]:
    return {name:age}    return {name:age}


def list_to_dict(words: List[str]) -> Dict[str, int]:def list_to_dict(words: List[str]) -> Dict[str, int]:
    dict_return={}    dict_return={}
    for i in range(len(words)):    for i in range(len(words)):
        dict_return[words[i]]=i        dict_return[words[i]]=i
    return dict_return    return dict_return



# don't modify code below this line# don't modify code below this line