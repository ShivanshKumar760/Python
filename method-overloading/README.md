# Method Overloading

**🔗 [View on NeetCode](https://neetcode.io/problems/python-method-overloading/question)**

---

**Method Overloading** is a feature that allows a class to have multiple methods with the same name, but different parameters. This is a form of polymorphism (one function name, multiple implementations).

```python
def method_name(parameter1, parameter2):
    pass

def method_name(parameter1, parameter2, parameter3):
    pass
```

In the above example, we have two methods with the same name `method_name`, but different parameters. Method overloading basically means that if you call `method_name` with two parameters, it will use the first method, and if you call it with three parameters, it will use the second method.

But there is a **problem** with this approach. Python **does not** support method overloading in the same way that languages like Java or C++ do.

#### The Solution

We can achieve method overloading in Python through default arguments or variable-length arguments.

```python
class Calculator:
    # Method 1: Default arguments
    def add(self, a: int, b: int, c: int = 0) -> int:
        return a + b + c

    # Method 2: Variable-length arguments
    def add_multiple(self, *args: int) -> int:
        return sum(args)
```

Example usage:

```python
calc = Calculator()

print(calc.add(5, 10))        # Output: 15
print(calc.add(5, 10, 15))    # Output: 30

print(calc.add_multiple(5, 10, 15, 20))    # Output: 50
print(calc.add_multiple(1, 2))             # Output: 3
```

The above code demonstrates two methods that achieve method overloading-like behavior.

1. **Using Default Arguments:**

- In the first `add` method, we make the third parameter optional by giving it a default value of 0

- This allows the method to work with either 2 or 3 arguments

- When called with 2 arguments, `c` defaults to 0

- When called with 3 arguments, all values are used

2. **Using Variable-Length Arguments:**

- The `add_multiple` method uses `*args` to accept any number of arguments

- The star `*` before `args` tells Python this method can accept any number of inputs. In the example, you can see that it accepts 4 and 2 arguments.

- We use the built-in `sum()` function to add all the numbers together

Remember that while this achieves similar results to traditional method overloading, it's not technically the same thing. Python will always execute the same method; we're just making that method flexible enough to handle different numbers of arguments.

#### Challenge

Given the definition of `TextProcessor` class, implement method overloading for `format_text` method. It should be able to take 1 or 2 arguments `text1` and `text2`.

- When given one word, it should convert it to uppercase. You can use the `upper()` method to convert a string to uppercase.

- When given two words, it should concatenate them and return the result. You can use the `+` operator to concatenate two strings.

**Expected Output:**

```
HELLO
helloworld
```

Hints

- Use default arguments to achieve method overloading by defaulting `text2` to `None`.

- Use the `text1.upper()` method to convert a string to uppercase.

- Use the `text1 + text2` to concatenate two strings.

- You can use `if text2 is None` to check if `text2` is not provided.

Looking for more? There's an advanced approach...

For those interested in exploring further, Python offers a more sophisticated way to handle method overloading using multiple dispatch. This advanced technique requires external libraries and is typically used in larger applications.

```python
from multipledispatch import dispatch

class Calculator:
    @dispatch(int, int)            # Method 1: Called when both args are integers
    def add(self, x, y):
        return f"Adding two ints: {x + y}"
    
    @dispatch(str, str)            # Method 2: Called when both args are strings
    def add(self, x, y):
        return f"Joining two strings: {x + y}"

calc = Calculator()
calc.add(1, 2)      # Calls Method 1 -> "Adding two ints: 3"
calc.add("a", "b")  # Calls Method 2 -> "Joining two strings: ab"
```

Python automatically picks the right method based on the argument types. You would need to install the `multipledispatch` library  using `pip install multipledispatch` to use this approach.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
