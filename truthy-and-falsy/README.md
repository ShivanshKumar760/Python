# Truthy and Falsy

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-truthy-and-falsy/question)

---

## 📋 Problem Description

In Python it's possible to use non-boolean values to execute conditional statements.

This is because Python has the concept of truthy and falsy values. A value is considered truthy if it evaluates to True in a boolean context. A value is considered falsy if it evaluates to False in a boolean context. The condition in an if statement is considered a boolean context.

A value is falsy if it is: False (boolean)

None (NoneType)

0 (integer)

0.0 (float)

"" (empty string)

[] (empty list)

Most other empty collections (e.g. empty tuple, empty set, empty dictionary) A value is truthy if it is: True (boolean)

All integers other than 0

All floats other than 0.0

All strings other than ""

All collections with at least one element This means that the following two if statements are equivalent:

As a beginner, it may be fine for you to prefer the second form, as it is more explicit. But be aware that the first form is more idiomatic in Python (more common and the intended way to use Python).

ChallengeImplement the function is_truthy(value) that returns "Truthy" if the value is truthy, and returns "Falsy" if the value is falsy. The parameter value can be any type of value. What other boolean contexts are there? Besides the condition in an if statement, there are other contexts where a value is evaluated as a boolean. For example, when using the logical operators and, or, and not, the values are evaluated as booleans. The boolean context is also used in loops, which we will cover soon.

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
