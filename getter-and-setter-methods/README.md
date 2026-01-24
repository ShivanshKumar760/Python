# Getter and Setter Methods

**🔗 [View on NeetCode](https://neetcode.io/problems/python-getter-and-setter-methods/question)**

---

Remember our `SuperHero` class? We used a private attribute `__power_level` and accessed it through a method:

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name                # private attribute
        self.__power_level = power_level  # private attribute
    
    # method to get power_level
    def get_power_level(self) -> int:      
        return self.__power_level
```

This method `get_power_level()` is what we call a **getter** - it's a method that returns (gets) the value of a private/protected attribute.

Similarly, a **setter** is a method that sets (changes) the value of a private or protected attribute.

Let's add a setter method to our SuperHero class with validation:

```python
def set_power_level(self, new_level: int) -> None:  # method to set power_level
    if 0 <= new_level <= 100:          # validation
        self.__power_level = new_level
    else:
        print("Power level must be between 0 and 100!")
```

The above method not only sets the value of the private attribute, but also validates the value. We specically check if the new value is in between `0` and `100` using `0 <= new_level <= 100` in the `if` statement. If the value is not in the range, we print an error message in the `else` block.

This ensures we never set an invalid value for the power level. This is another reason we prefer using methods to access and modify private attributes.

Alternatively, we could have raised an error using `raise ValueError("Power level must be between 0 and 100!")` instead of printing an error message.

#### Example Usage

```python
hero.set_power_level(90)   # Changes to 90
hero.set_power_level(150)  # Error: Power level must be between 0 and 100!
```

#### Challenge

You are given a `BankAccount` class. Your task is to:

1. Add a private attribute named `__balance` which is initialized in the constructor. It should store an integer value.

2. Add a getter method for balance named `get_balance() -> int` that returns the balance.

3. Add a setter method for balance named `set_balance(new_balance: int) -> None` that sets the value of balance if it is non-negative. If the balance is negative print `Cannot set negative balance!` and do *not* update the balance.

**Expected Output**

```
1000
Cannot set negative balance!
1000
100
0
```

Hints

- Use double underscore for private balance

- Getter just returns the private balance

- Setter should check if new balance >= 0

Best Practices

- Always use the name `get_<attribute>` for getter methods

- Always use the name `set_<attribute>` for setter methods

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
