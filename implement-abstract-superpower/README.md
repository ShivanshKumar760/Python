# Implement Abstract Superpower

**🔗 [View on NeetCode](https://neetcode.io/problems/python-implement-abstract-superpower/question)**

---

Given the code below, implement the `Superpower` abstract class. The `Superpower` class should have:

- A constructor that accepts two parameters: `name` and `power_level`

- An `is_active` instance variable that is initialized to `False`

- A concrete `get_power_level` method that returns the `power_level` as an integer.

- An abstract `activate` method.

- An abstract `deactivate` method.

**Expected Output:**

```
10
8
Laser Beam activated!
Super Strength activated!
Laser Beam deactivated!
Super Strength deactivated!
```

Hints

- Use the `ABC` class from the `abc` module to define the `Superpower` class as an abstract class.

- Use the `abstractmethod` decorator from the `abc` module to define the `activate` and `deactivate` methods as abstract methods.

- As the `Superpower` class is abstract, you can implement the `get_power_level` method as a concrete method.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
