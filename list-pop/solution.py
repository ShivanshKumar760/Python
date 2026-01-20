"""
Problem: List Pop
URL: https://neetcode.io/problems/python-list-pop/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List # this is used to add type hints for List typefrom typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:def remove_from_list(my_list: List[int], index: int) -> List[int]:
    my_list.pop(index)    my_list.pop(index)
    return my_list    return my_list


# def pop_n_from_list(my_list: List[int], n: int) -> List[int]:# def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
#     for i in range(n,0,-1):#     for i in range(n,0,-1):
#         my_list.pop(-i)#         my_list.pop(-i)
#     return my_list#     return my_list
def pop_n_from_list(my_list: List[int], n: int) -> List[int]:def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    for i in range(n):    for i in range(n):
        my_list.pop()        my_list.pop()
    return my_list    return my_list



# don't modify below this line# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))print(pop_n_from_list([1, 2, 3, 4, 5], 5))
