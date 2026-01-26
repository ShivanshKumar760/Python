# Class Methods

**🔗 [View on NeetCode](https://neetcode.io/problems/python-class-methods/question)**

---

So far the methods we have used were all related to the instance of the class. For example, we used `use_power` method which was used by a single superhero.

Sometimes we need special methods that work with the entire class rather than individual instances. For example, we may want to upgrade the training level of all heroes at once. Let's see how we can do that using class methods.

```python
class Superhero:
    training_level = 1  # Class attribute
    
    def __init__(self, name: str, power: str):
        self.name = name         # Instance attribute
        self.power = power       # Instance attribute
        
    @classmethod
    def upgrade_training(cls) -> None:
        cls.training_level += 1
        print(f"All heroes now at training level {cls.training_level}")
```

In the above `Superhero` class, the `upgrade_training` method is a class method.

- It uses `@classmethod` decorator to define the class method

- It uses `cls` as the first parameter instead of `self`

- It upgrades the `training_level` (a class attribute) by `1`

- `cls` is used to access the class attribute instead of the class name `Superhero`

The below code shows how the recommended way to call the class method:

```python
Superhero.upgrade_training()     # Recommend way to use class method
print(Superhero.training_level)  # 2
```

The below code shows how the class method can be called using an instance of the class, which is *not* recommended:

```python
iron_man = Superhero("Iron Man", "Flying")
iron_man.upgrade_training()     # Works but not recommended
print(iron_man.training_level)  # 2
```

**Important**: Class methods are similar to class attributes. They are shared by all instances of the class. This also means that they do *not* have access to instance attributes, which is why we don't use `self` in class methods. Class methods can be defined with additional parameters, after the `cls` parameter.

#### Challenge

Given the code for `Library` class, implement the following two class methods to manage book lending.

- `lend_books` that takes `number` as an argument and subtracts it from `books_available`

- `return_books` that takes `number` as an argument and adds it to `books_available`

**Expected Output**

```
Initial status: 100 books available
After lending: 70 books available
After return: 80 books available
```

Hint

- Always pass `cls` as the first parameter to the class method

- Use `cls.books_available` to access the class attribute

- Use `cls.books_available -= number` to decrease the number of books available

- Use `cls.books_available += number` to increase the number of books available

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
