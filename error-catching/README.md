# Error Catching

**🔗 [View on NeetCode](https://neetcode.io/problems/python-error-catching/question)**

---

When an error occurs in a `try` block, it may be useful for us to know exactly what error occurred. This can allow us to better debug our code.

```python
try:
    result = 10 / 0
except Exception as error:
    print("Error:", error)
```

The above code will *catch* the error and place it inside a variable called `error` using the `as` keyword. We can then print this variable to see the error message, which would be:

```plaintext
Error: division by zero
```

#### Challenge

Implement the function `divide_numbers(a: str, b: str) -> None`. It accepts two strings as arguments. You should attempt to convert the strings into integers, and then divide the first number by the second number. And then print the result.

If an error occurs, print `"An error occurred:"`, followed by the error message.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
