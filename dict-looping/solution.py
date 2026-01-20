"""
Problem: Dict Looping
URL: https://neetcode.io/problems/python-dict-looping/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Dict, List # this adds type hints for List and Dictfrom typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    dict2List=[]    dict2List=[]
    for i in age_dict:    for i in age_dict:
        dict2List.append(i)        dict2List.append(i)
    return dict2List    return dict2List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    dict2ListV=[]    dict2ListV=[]
    for i in age_dict:    for i in age_dict:
        dict2ListV.append(age_dict[i])        dict2ListV.append(age_dict[i])
    return dict2ListV    return dict2ListV

# do not modify below this line# do not modify below this line