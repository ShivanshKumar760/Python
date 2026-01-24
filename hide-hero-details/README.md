# Hide Hero Details

**🔗 [View on NeetCode](https://neetcode.io/problems/python-hide-hero-details/question)**

---

In this challenge, you'll refactor the `SuperHero` class to hide the hero's attributes. The goal is to protect the hero's attributes while providing controlled access to them. Your tasks are:

#### 1. In the `SuperHero` class `init` method:

- Add the private attributes `health` and `power_level`.

#### 2. Implement the following methods:

- Implement a method `get_health` that returns the hero's health.

- Implement a method `get_power_level` that returns the hero's power level.

- Implement a method `set_health` that sets the hero's health if it is within the range `0 - 100` inclusive.

- If the health is greater than 100 print `You can't set the health to more than 100`.

- If the health is less than 0 print `You can't set the health to less than 0`.

- Otherwise set the health.

- Implement a method `set_power_level` that sets the hero's power level if it is within the range `1 - 10` inclusive.

- If the power level is greater than 10 print `You can't set the power level to more than 10`.

- If the power level is less than 1 print `You can't set the power level to less than 1`.

- Otherwise set the power level.

#### 3. Print the hero's attributes. Use the following format: `{hero's name} has {health} health and {power_level} power level`.

- Do this without accessing the private attributes directly.

Note: For this challenge, do **not** use the `@property` or `@name.setter` decorators. You will practice using them in the next challenge.

#### Expected Output

```
80
You can't set the health to more than 100
You can't set the health to less than 0
9
You can't set the power level to more than 10
You can't set the power level to less than 1
Batman has 70 health and 7 power level
```

Hints

- Use the `__` prefix to make the attributes private

- Use the getter and setter methods to access the private attributes

- Use the  `get` keyword to implement the getter methods

- Use the  `set` keyword to implement the setter methods

- You can't print the private attributes directly use the getter methods to access them

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
