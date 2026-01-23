# Docstrings

**🔗 [View on NeetCode](https://neetcode.io/problems/python-docstrings/question)**

---

Docstrings are string literals that describe functions, methods, classes, or modules. They serve as documentation for our code.

Let's see an example:

```python
class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        health (int): The superhero's health points
    """

    def __init__(self, name: str, health: int) -> None:
        """Initialize a new SuperHero instance."""
        self.name = name
        self.health = health

    def take_damage(self, amount: int) -> None:
        """
        Reduce the superhero's health by the given amount.

        Args:
            amount (int): The amount of damage to inflict
        """
        self.health -= amount
        print(f"{self.name} takes {amount} damage.")
```

We have three docstrings in this class:

1. The class docstring describes the class and its attributes.

2. The `__init__` method docstring describes the method and its parameters.

3. The `take_damage` method docstring describes the method and its parameters.

#### Writing Docstrings

For both classes and methods:

- Use triple quotes (""") to enclose the docstring

- Place the docstring immediately after the class or method definition

- Follow a consistent style (e.g., Google-style)

For classes:

- Describe the purpose of the class

- List and explain attributes

For methods:

- Use a one-line description for simple methods

- For complex methods:

- Describe what the method does

- List and explain parameters (Args:)

- Describe the return value (Returns:)

- Mention any exceptions raised (Raises:)

#### Using Docstrings

```python
# Print the class docstring
print(SuperHero.__doc__)

# Get help on the whole class (includes docstrings of class and methods)
help(SuperHero)

# Print a method's docstring
print(SuperHero.take_damage.__doc__)
```

By adding docstrings, you make your code more understandable for future users, including yourself.

#### Challenge

When you run the code, you'll see `None` printed for each docstring because they don't exist yet. Your tasks are as follows:

1. Write a class docstring describing what the `Pet` class represents.

2. Add a brief docstring to the `__init__` method.

3. Add a docstring to the `make_sound` method explaining what it does.

Remember to use triple quotes for your docstrings.

#### Expected Output

```
A class to represent a pet.

    Attributes:
        name (str): The pet's name
        animal_type (str): The pet's type
    
Initialize a new Pet instance.
Return the sound the pet makes based on its type.
```

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
