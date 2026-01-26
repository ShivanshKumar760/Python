# Implement Power Calculation System

**🔗 [View on NeetCode](https://neetcode.io/problems/python-implement-power-calculation-system/question)**

---

Suppose we are developing a game where we need to calculate the effective power level of a hero when creating it. You are given the `Hero` class and its `__init__` method. Your tasks are:

#### 1. Add a static method `calculate_effective_power` that takes two parameters:

- `base_power`: The hero's base power level (integer)

- `attributes`: A dictionary containing the hero's attributes (strength, speed, intelligence)

The method should:

1. Calculate the `attribute_bonus` by averaging all attribute values. Use `sum(attributes.values()) / len(attributes)` to calculate the average

2. Calculate effective power using the formula: `base_power * (1 + attribute_bonus)`

3. Round the final result to one decimal place. Use `round(number, 1)` to round to one decimal place

4. Return the calculated effective power

**Expected Output:**

```
Base Power: 8
Attributes: {'strength': 7, 'speed': 6, 'intelligence': 8}
Effective Power: 64.0

Base Power: 6
Attributes: {'strength': 4, 'speed': 5, 'intelligence': 6}
Effective Power: 36.0
```

Hints

- Use the `@staticmethod` decorator to define the static method

- Don't pass `self` or `cls` as a parameter to the static method

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
