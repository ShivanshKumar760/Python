# Type Conversion with Input

**🔗 [View on NeetCode](https://neetcode.io/problems/python-type-conversion-input/question)**

---

We are not required to provide a prompt to the user when calling the `input()` function:

```python
user_input = input() # This will read one line of input from stdin

print(user_input) # This will print the input to the console
```

By default, `input()` returns the user input as a *string*. If you're expecting a different type of input like an *integer* or a *float*, you need to explicitly convert it using `int()` or `float()`.

```python
age = int(input("Enter your age: "))

temperature = float(input("Enter the temperature: "))
```

The example above converts the user input, which is expected to be an *integer* representing age, to an *integer* using `int()`. It also converts the user input, which is expected to be a *float* representing temperature, to a *float* using `float()`. It's important to note that if the user enters a value that can't be converted to the expected type, a `ValueError` will be raised, so be careful when converting user input.

#### Challenge

Implement the following two functions:

1. `read_integer() -> int`: This function should read an integer from the user and return it. The prompt should be *empty*.

2. `read_float() -> float`: This function should read a floating point number from the user and return it. The prompt should be *empty*.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
