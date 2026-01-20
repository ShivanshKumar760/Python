"""
Problem: List Looping
URL: https://neetcode.io/problems/python-list-looping/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    count=0
    for element in nums:
        if(element==x):
            count+=1
        else:
            continue
    return count

# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
