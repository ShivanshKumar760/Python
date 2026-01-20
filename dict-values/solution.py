"""
Problem: Dict Values
URL: https://neetcode.io/problems/python-dict-values/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Dict, Listfrom typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    getValue=[]    getValue=[]
    for value in age_dict.values():    for value in age_dict.values():
        getValue.append(value)        getValue.append(value)
    return getValue    return getValue

# do not modify below this line# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
