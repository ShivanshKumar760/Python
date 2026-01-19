# Reversing a String

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-reversing-a-string/question)

---

## 📋 Problem Description

We can also use slicing to reverse a string. By not specifying the starting index or the ending index, and setting the step to -1, the string will be reversed.

Take a look at the example below:

Notice that we have two colons in the slicing syntax. This will make more sense if you look at the below example:

The value before the first colon is the starting index, the value after the first colon is the ending index, and the value after the second colon is the step. If the step is negative, the string will be reversed.

Remember that the starting index is inclusive, and the ending index is exclusive, even when the step is negative.

ChallengeImplement the function reverse_string(input_string: str) -> str. It takes a string as a parameter and returns the reversed string.

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
