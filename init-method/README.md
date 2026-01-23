# Init Method

**🔗 [View on NeetCode](https://neetcode.io/problems/python-init-method/question)**

---

The `__init__` method we've been using is a special method in Python classes, also known as a constructor. Its job is to initialize the attributes of a new object when it's created.

The `__init__` method is technically *not* a constructor in Python, but it's often referred to as one. The `__new__` method is the actual constructor in Python.

```python
class SuperHero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
```

The `__init__` method is automatically called when we create a new object from our class. It sets up the initial state of the object.

In the above code, `__init__` is responsible for setting the initial values for `name` and `power` for each new superhero we create.

```python
# Creating a superhero
iron_man = SuperHero("Iron Man", "repulsor beams")
```

Above we created a `SuperHero` object called `iron_man` which calls the `__init__` method. Logically, this is equivalent to `SuperHero.__init__(iron_man, "Iron Man", "repulsor beams")`

- We don't need to explicitly pass anything for the `self` parameter because Python handles this automatically.

- `self` inside `__init__` refers to the new `iron_man` object

- The other parameters are passed to the `__init__` method to initialize the attributes of the object

After this process, `iron_man` is a fully initialized `SuperHero` object with all its attributes set.

#### Challenge

We have a `Pet` class, but its `__init__` method is missing. Currently, the code will produce the following error when you try to run it.

```
TypeError: Pet() takes no arguments
```

Your task is add the `__init__` method to the `Pet` class to initialize the `name`, `species`, and `age` attributes when a new pet is created.

#### Expected Output

```
Fluffy is a 3 year old cat.
Buddy is a 2 year old dog.
```

Hints
- The `__init__` method is called automatically when creating a new object.
- Think about the parameters the `__init__` method should have.

Key Points About `self` and `__init__`

- The `**init**` method is automatically called when creating a new object.

- `self` is always the first parameter in method definitions, including `**init**`.

- When creating objects or calling methods, we don't explicitly provide `self` - Python handles this automatically.

- Inside `**init**`, `self` refers to the newly created object.

- Use `**init**` to set initial values for the object's attributes.

Attributes outside of `__init__`

- Attributes outside of `**init**` and other methods are class attributes, shared by all instances of the class.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
