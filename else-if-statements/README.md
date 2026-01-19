# Else-If Statements

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-elif/question)

---

## 📋 Problem Description

We can create a chain of conditional statements using the elif keyword (standing for else-if). This allows us to check multiple conditions in order, until one of them is true. Here's an example:

Python will check each condition from top to bottom until one of them executes. In this case none of the first three conditions is True so the else block will execute. If the balance was -10, the if statement would execute, and the others would be skipped.

If the balance was 0, the first elif statement would execute, and the others would be skipped.

If the balance was 50, the second elif statement would execute, and the others would be skipped.

By the time we reach the else statement, we know the balance is not negative, zero, or less than 100, so it must be greater than or equal to 100. ChallengeIn the code editor, using if, elif and else, implement the function called check_range(num: int) -> str. If num is less than 0, return the string "negative".

If num is 0 return the string "zero".

If num is greater than 0 and less than 10, return the string "positive single digit".

If num is greater than or equal to 10, return the string "positive multi digit".

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
