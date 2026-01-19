# Type Hints

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-type-hints/question)

---

## 📋 Problem Description

In Python, you can add type hints to your functions to indicate what type of data the function expects to receive and return. This is not required, but it can be helpful for other developers who are reading your code.

To add a type hint for a parameter, you add a colon after the parameter name and then the type of data you expect. To add a return type, you add a right arrow (->) after the closing parenthesis and then the type of data you expect to return (before the colon).

Type hints don't change how the function works, for example, we could still pass a couple of strings to the add function above and it would still work.

What if we had a function that did not return anything? The return type would be None.

If you don't believe me, you can confirm it yourself.

ChallengeIn the code editor, call the function greet with the argument "NeetCode". Then print the type of the return value of the function. Hint: You can get the type of a value with the type() function. What if we explicitly return None? Whether we don't return anything from a function, or explicitly return None, or even have an empty return statement, the return value will be None in all cases.

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
