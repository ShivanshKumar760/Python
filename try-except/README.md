# Try Except

**🔗 [View on NeetCode](https://neetcode.io/problems/python-try-except/question)**

---

When an error occurs in a program, it usually causes the program to crash. And Python is no exception.

```python
result = 10 / 0 # ZeroDivisionError: division by zero

print("This will not be printed.")
```

But there is a way we can handle these errors and prevent the program from crashing. This is done using the `try` and `except` blocks.

```python
try:
    # code that might cause an error
    result = 10 / 0
except:
    print("An error occurred!")

print("This will be printed regardless.")
```

A `try` block is reminiscent to an `if-else` statement. The code inside a `try` block is always executed, but if any line of code raises an error, the program will immediately jump to the `except` block. If no error occurs, the `except` block is skipped.

This is called **exception handling**.

#### Challenge

Implement the function `divide_numbers(a: int, b: int) -> None`. It should attempt to divide `a` by `b` and print the result. If an error occurs, print `"An error occurred!"`.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
