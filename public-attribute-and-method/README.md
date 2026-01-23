# Public Attribute and Method

**🔗 [View on NeetCode](https://neetcode.io/problems/python-public-attribute-and-method/question)**

---

In Python, public attributes or methods can be accessed and modified directly from outside the class. By default, *all* attributes and methods in Python are **public**.

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.name = name                # public attribute
        self.power_level = power_level  # public attribute
    
    # Public method
    def display_power_level(self) -> None:
        print(f"{self.name} has a power level of {self.power_level}")
```

When an attribute or method is public, we can:

- Access it directly using dot notation

- Modify the attribute from outside the class

- Call the method from outside the class

Let's see public attributes in action:

```python
# Creating a superhero
spider_man = SuperHero("Spider-Man", 85)

# Accessing public attributes/methods
print(spider_man.name)
spider_man.display_power_level()

# Modifying public attributes
spider_man.power_level = 90
```

Public attributes are suitable when:

- The attribute doesn't need validation

- Direct access won't compromise the object's integrity

- You want to keep the code simple and straightforward

Don't worry about the above for now, we will cover validation and integrity later.

#### Challenge

You are given starter code for a simple shop system where items are displayed with their names and prices. Your tasks are:

- Add public attributes for name and price

- Access the attributes of the `chips` object and display them. Use this format: `Item: [name] - Price: $[price]` for printing.

```python
class StoreItem:
    def __init__(self):
        pass  # Add: name, price

chips = StoreItem("Chips", 1.99)
```

**Expected Output**

```
Chips
1.99
```

Hints

- Remember to initialize attributes in the **init** method

- Use descriptive names for your attributes

- Public attributes can be accessed using dot notation

- Use the `print` function to display the attributes

What is Encapsulation?

- Encapsulation is the concept of wrapping data and methods that work on the data within one unit, called a class. In addition, it restricts access to some of the object's components.

- The purpose is to hide the internal details of an object and only expose the necessary parts of the object to the outside world.

- A real world analogy is a car. The car is a complex system with many moving parts. However, as a driver, you don't need to know how the car works internally. You only need to know how to operate the car.

Key Points About Public Attributes

- Public attributes are accessible from anywhere in the code

- They're defined without any special naming convention

- They offer direct access to object properties

- They're suitable for simple, straightforward data storage

- No special methods are needed to access or modify them

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
