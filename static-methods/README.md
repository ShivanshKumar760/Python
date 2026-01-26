# Static Methods

**🔗 [View on NeetCode](https://neetcode.io/problems/python-static-methods/question)**

---

So far we've seen instance methods (using `self`) and class methods (using `cls`).

There are also **static methods** which are similar to class methods but they don't have access to `self` or `cls`. They do not have access to instance attributes, but they *can* still access class attributes using the class name.

They are just regular functions that live inside a class for organizational purposes.

```python
class Superhero:
    def __init__(self, name: str, power: str):
        if not self.is_valid_power(power):
            raise ValueError(f"Invalid power: {power}")
        self.name = name        # Instance attribute
        self.power = power      # Instance attribute
    
    @staticmethod
    def is_valid_power(power: str) -> bool:
        valid_powers = ['Flying', 'Strength', 'Speed', 'Intelligence']
        for valid_power in valid_powers: # Iterate over each valid power and check if the power matches
            if power == valid_power:
                return True
        return False
```

In the above code, we defined a class `Superhero` with a static method `is_valid_power`. We call this method using the `self` parameter within the `__init__` method for validation before creating the hero.

Alternatively, we could have defined this method outside the class, but this method would never be needed outside the class. Thus, it's best to define it inside the class for organizational purposes.

Below is an example of how this class can be used. Notice that we can also call the static method using the class name.

```python
print(Superhero.is_valid_power('Flying'))         # True
print(Superhero.is_valid_power('Mind Reading'))   # False

iron_man = Superhero("Iron Man", "Flying")        # Works

mind_reader = Superhero("Hero", "Mind Reading")   # Raises ValueError
```

#### Challenge

Complete the `CurrencyConverter` class to convert between currencies using static methods. You are already given the `rates` class attribute which you can use to convert between currencies. Your tasks is to:

1. Implement the static method `to_usd`  that takes an amount and a currency code as arguments and converts the amount to USD and returns the converted amount.

#### Expected Output

```
100 EUR = 120.0 USD
100 JPY = 1.0 USD
```

Hints

- Use `@staticmethod` decorator to define the static methods

- Use the `rates` dictionary to convert between currencies

- You don't need to pass `self` or `cls` as the first parameter in static methods

- Use the `CurrencyConverter.rates` to access the `rates` class attribute in the static methods

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
