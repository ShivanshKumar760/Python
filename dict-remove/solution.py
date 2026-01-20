"""
Problem: Dict Remove
URL: https://neetcode.io/problems/python-dict-remove/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Dict, Listfrom typing import Dict, List
# You’re iterating over a dictionary and modifying it at the same time (del my_dict[i] while looping).# You’re iterating over a dictionary and modifying it at the same time (del my_dict[i] while looping).
# That’s why Python throws RuntimeError: dictionary changed size during iteration.# That’s why Python throws RuntimeError: dictionary changed size during iteration.
# def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:# def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
#     for i in my_dict:#     for i in my_dict:
#         if i in keys:#         if i in keys:
#             del my_dict[i]#             del my_dict[i]
#     return my_dict#     return my_dict
def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    dictKeyList=list(my_dict.keys())    dictKeyList=list(my_dict.keys())
    # print(dictKeyList)    # print(dictKeyList)
    for i in dictKeyList:    for i in dictKeyList:
        if i in keys:        if i in keys:
            del my_dict[i]            del my_dict[i]
    return my_dict    return my_dict