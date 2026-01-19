# String Formatting

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-string-formatting/question)

---

## 📋 Problem Description

We saw that we can concatenate strings using the + operator. However, this can be cumbersome when we have many strings to concatenate. Python provides a more elegant way to format strings using the format method.

In the above code, we have a string with two placeholders: {}. We then call the format method on the string and pass in the values we want to replace the placeholders with. The values are passed in the order they are to be inserted. The number of placeholders must match the number of arguments passed to the format method.

You can also use the index of the placeholders to specify the order of the arguments.

An even more concise way to format strings is to use f-strings. These are prefixed with an f before the string and allow you to insert variables directly into the string.

ChallengeImplement the function say_goodbye(name: str, hour: int) -> str that returns a string in the following format:

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
