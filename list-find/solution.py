"""
Problem: List Find
URL: https://neetcode.io/problems/python-list-find/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List # this is used to add type hints for List typefrom typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:def find_index(nums: List[int], target: int) -> int:
    return nums.index(target)    return nums.index(target)
    # for i in range(len(nums)):    # for i in range(len(nums)):
    #     if nums[i]==target:    #     if nums[i]==target:
    #         return i    #         return i


# don't modify code below this line# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))print(find_index([1, 3, 4, 2], 2))

