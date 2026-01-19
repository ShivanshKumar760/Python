# Strings are Immutable

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-strings-are-immutable/question)

---

## 📋 Problem Description

It's important to know that whenever you slice a string, you are not modifying the underlying string. Instead, you are creating a new string with the sliced characters. This is because strings are immutable in Python, which means they cannot be changed after they are created.

In the above code, we try to reassign just the first character of the string. This will cause a TypeError because strings are immutable. We cannot change individual characters, we can only reassign the entire string.

If we wanted to create a new string with the second character removed, we can accomplish this by slicing and concatenation.

Above, we removed the second character from the string (which was the space " "), and concatenated the two parts together to create a new string.

ChallengeImplement the function remove_fourth_character(word: str) -> str, which removes the fourth character from the string and returns the new string. You may assume that the length of the string is greater than 4.

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
