# Implement Area Calculator

**🔗 [View on NeetCode](https://neetcode.io/problems/python-implement-area-calculator/question)**

---

You are given an empty `AreaCalc` class. Implement a method `calculate(length, width=None)` that handles two types of area calculations:

1. When given one argument (radius), it should calculate circle area:

- Use the formula: π * r². You can use `math.pi` to get the value of π.

- The result should be rounded to 2 decimal places. You can use the `round(n, 2)` function to round the result to 2 decimal places.

2. When given two arguments (length, width), it should calculate rectangle area:

- Use the formula: `length * width`

- Return the result as is

**Note:**

- You can use `*args` or `arg1, arg2` to handle the two cases. Both are valid.

**Expected Output:**

```
78.54
24
```

Hints

- Use `round(result, 2)` to format circle area to 2 decimal places

- Check the number of arguments to determine which formula to use

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
