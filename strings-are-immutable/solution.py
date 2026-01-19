"""
Problem: Strings are Immutable
URL: https://neetcode.io/problems/python-strings-are-immutable/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def remove_fourth_character(word: str) -> str:
    return word[:3] + word[4:]


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
