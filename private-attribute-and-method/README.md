# Private Attribute and Method

**🔗 [View on NeetCode](https://neetcode.io/problems/python-private-attribute-and-method/question)**

---

**Private** attributes and methods are class members that should not be accessed from outside the class. They are denoted by prefixing the attribute/method name with double underscores (__).

Unlike protected attributes, they are **not accessible** from child classes. We will learn about child classes in the inheritance chapter.

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name                # private attribute
        self.__power_level = power_level  # private attribute
    
    # private method
    def __secret_power(self) -> str:        
        return f"Using {self.__name}'s secret power!"
        
    # public method to access private method
    def use_power(self) -> str:             
        return self.__secret_power()
    
    # public method to access private attribute
    def get_power_level(self) -> int: 
        return self.__power_level
```

In the above code, the `__name` and `__power_level` attributes are private, meaning they cannot be accessed directly from outside the class. The same goes for the `__secret_power` method. Though we can access them using the public methods `get_power_level` and `use_power`.

When an attribute/method is private:

- It should not be directly accessed using normal dot notation from outside the class.

- It's meant to be used only within the class itself.

- It provides the strongest form of information hiding in Python.

#### Challenge

You are given the code for the `PasswordManager` class. Your task is to:

1. Add a private attribute for storing the password, which should be a string initialized in the constructor.

2. Implement a public method `verify_password` that takes an input password and returns `True` if it matches the stored password, otherwise  return `False`.

**Expected Output**

```
True
False
```

Hints

- Use double underscores (__) for private attributes

- Remember private attributes can only be accessed within the class

Key Points About Private Attributes

- Private attributes are denoted by double underscores (__)

- They should be accessed only through public methods

- They're ideal for sensitive information e.g passwords

Summary
- Public (no underscore): Accessible everywhere
- Protected (single underscore `_` ): Should only be accessed within class and subclasses
- Private (double underscore `__` ): Should only be accessed within the defining class

Remember though, Python follows the **we're all consenting adults** philosophy - these are conventions rather than strict rules. Private/protected attributes can still be accessed, but doing so is strongly discouraged.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
