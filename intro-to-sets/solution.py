"""
Problem: Intro to Sets
URL: https://neetcode.io/problems/python-intro-to-sets/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List, Set # this adds type hints for List and Setfrom typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:def list_to_set(nums: List[int]) -> Set[int]:
    my_set=set()    my_set=set()
    for item in nums:    for item in nums:
        my_set.add(item)        my_set.add(item)
    return my_set    return my_set
# do not modify below this line# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
