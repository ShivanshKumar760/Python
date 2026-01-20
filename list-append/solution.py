"""
Problem: List Append
URL: https://neetcode.io/problems/python-list-append/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List # this is used to add type hints for List typefrom typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    for i in elements:    for i in elements:
        my_list.append(i)        my_list.append(i)
    return my_list    return my_list



# do not modify below this line# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))print(append_to_list([], [1, 2, 3, 4]))
