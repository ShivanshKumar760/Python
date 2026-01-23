# Protected Attribute and Method

**🔗 [View on NeetCode](https://neetcode.io/problems/python-protected-attribute-and-method/question)**

---

In Python, **protected** attributes and methods are class members that should *not* be accessed directly from outside the class. However, they can be accessed within the class and in child classes (see below for more on child classes).

Protected attributes are denoted by prefixing the attribute/method name with a single underscore `_`.

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self._name = name                # protected attribute
        self._power_level = power_level  # protected attribute
        
    def get_name(self) -> str: # public method
        return self._name

    def _some_protected_method(self) -> None: # protected method
        pass

    def some_public_method(self) -> None:
        self._some_protected_method()
```

Unlike other languages, Python doesn't enforce access control for protected attributes. We can still access them directly, but it's not recommended. Using an underscore prefix is a convention to signal to other developers that these attributes shouldn't be accessed directly from outside.

Below is the recommended way to access protected attributes and methods:

```python
spider_man = SuperHero("Spider-Man", 85)

print(spider_man._name)      # Allowed but discouraged
print(spider_man.get_name()) # Recommended

spider_man._some_protected_method() # Allowed but discouraged
spider_man.some_public_method()     # Recommended
```

1. To access protected attributes, use the public methods.

2. To access protected methods, use the public methods.

#### Challenge

You are given code for a simple banking system. Your task is to:

- Initialize two attributes, "title" a public attribute and "_balance" a protected attribute

- Use a public method `display_balance` to display the balance.

**Expected Output**

```
Balance: $1000
```

Hints

- Use underscore prefix for protected attributes during initialization

- Remember you can access protected attributes within the class.

- Remember protected attributes are still accessible but shouldn't be accessed directly

What's a child class?
A child class is a class that inherits attributes and methods from another class (called the parent class). We'll cover inheritance in detail in upcoming lessons, but for now, just know that protected members are not accessible outside of a class or its child classes.

Remember

Python doesn't enforce protection through technical restrictions, protected attributes (prefixed with `_`) act as a convention - similar to a yellow traffic light. They warn other developers: **You can access this, but you probably shouldn't**

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
