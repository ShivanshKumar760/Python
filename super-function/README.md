# Super Function

**🔗 [View on NeetCode](https://neetcode.io/problems/python-super-function/question)**

---

`super()` is a built-in function in Python that allows you to call methods from a parent class. It's a powerful tool for working with inheritance.

#### Why use `super()`?

When working with inheritance, there are often situations where you want to extend rather than completely replace a parent class's behavior. For example:

- You might want to add extra initialization steps while keeping the parent's initialization

- You may need to enhance an existing method while maintaining its core functionality

- You could need to access parent class properties while adding new ones

Let's see an example:

```python
class ParentClass:
    def parent_method(self) -> None:
        print("This is the parent class method")

class ChildClass(ParentClass):
    def child_method(self) -> None:
        super().parent_method()
        print("This is the child class method")
```

In this example, the `super()` function is used to call the `parent_method` from the `ParentClass`. The `super()` method can be visualized as an object that points to the parent class. Remember `super()` itself doesn't take any arguments, but it can be used to call the parent class's methods.

#### Syntax for `super()` function

```python
super().parent_method() # Call parent class's instance method

super().__init__() # Call parent class __init__ method

super().parent_property # Access parent class property
```

#### Challenge

Given the code for the `SuperHero` class, complete the following tasks:

1. Create an `Avenger` class that inherits from the `SuperHero` class.

2. Override the `__init__` method to add a `team` property to the `Avenger` class. `Avenger` should also call the `__init__` method of the `SuperHero` class to initialize the `name` and `power` properties.

3. Define the `attack` method in the `Avenger` class, which should call the `attack` method of the `SuperHero` class.

**Expected Output**

```
Iron Man
repulsor beams
Avengers
Iron Man is attacking with repulsor beams
```

Hints

- Use the `super().__init__(name, power)` function to call the `__init__` method of the `SuperHero` class.

- Use the `super().attack()` function to call the `attack` method of the `SuperHero` class.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
