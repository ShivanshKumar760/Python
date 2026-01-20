# Multiple Except Blocks

**🔗 [View on NeetCode](https://neetcode.io/problems/python-multiple-except-blocks/question)**

---

Instead of having a single `except` block to handle all exceptions,

```python
try:
    n = 10 / 0
except Exception as error:
    print("An error occurred:", error)
```

you can have multiple `except` blocks to handle different types of exceptions.

```python
try:
    num1 = int(a)
    num2 = int(b)
    result = num1 / num2
except ValueError:
    print("Error: Invalid value!")
except ZeroDivisionError:
    print("Error: Division by zero!")    
except Exception as error:
    print("An error occurred:", error)
```

In the first example we catch all exceptions with `Exception`. In the second example, we have different blocks to handle different exceptions. The first `except` will catch a `ValueError`, the second will catch a `ZeroDivisionError`, and the third will catch any other exceptions. That means, if neither a `ValueError` nor a `ZeroDivisionError` occurs, the third block will still catch all other exceptions.

#### Challenge

Implement the `divide_numbers(a: str, b: str) -> None` function. It accepts two strings as arguments. You should attempt to convert the strings into integers, and then divide the first number by the second number, and then print the result.

1. If a `ValueError` occurs, print `"Error: Invalid value!"`.

2. If a `ZeroDivisionError` occurs, print `"Error: Division by zero!"`.

3. If any other error occurs, print `"An error occurred:"`, followed by the error message.

  
    *What other types of exceptions are there?*
    

There are many built-in exceptions in Python. Some common ones include `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, and `ImportError`. You can also create your own exceptions.

    

You don't have to memorize all of them, but it's good to know that different types of exceptions exist. If needed, you can normally read logs to determine the type of exception that occurred. You can view a list of built-in exceptions in the Python documentation.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
