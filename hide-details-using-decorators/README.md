# Hide Details Using Decorators

**🔗 [View on NeetCode](https://neetcode.io/problems/python-hide-details-using-decorators/question)**

---

In this challenge, you'll refactor the `SuperHero` class to use property decorators.

You are given a `SuperHero` class. Your tasks are:

1. Inside the `SuperHero` class:

- Implement a `getter` for health using the `@property` decorator that returns the hero's health

- Implement a `getter` for power_level using the `@property` decorator that returns the hero's power level

- Implement a `health` setter using the `@setter` decorator with validation (0-100 range)

- If the health is greater than 100 print `You can't set the health to more than 100`

- If the health is less than 0 print `You can't set the health to less than 0`

- Otherwise set the health

- Implement a `power_level` setter using the `@setter` decorator with validation (1-10 range)

- If the power level is greater than 10 print `You can't set the power level to more than 10`

- If the power level is less than 1 print `You can't set the power level to less than 1`

- Otherwise set the power level

2. Print the hero's attributes. Use the following format: `{hero's name} has {health} health and {power_level} power level`.

**Expected Output**

```
80
You can't set the health to more than 100
9
You can't set the power level to more than 10
You can't set the power level to less than 1
Batman has 80 health and 9 power level
```

Hints

- You can use the methods from the previous challenge remember to use the `@property` decorator for the getter methods and the `@name.setter` decorator for the setter methods

- Use the `__` prefix to make the attributes private

- Use `@property` to create getter properties

- Use `@property_name.setter` to create setter properties

- The validation logic stays the same as in the original getter/setter methods

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
