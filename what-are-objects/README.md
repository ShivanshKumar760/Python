# What are Objects?

**🔗 [View on NeetCode](https://neetcode.io/problems/python-what-are-objects/question)**

---

An **object** is an instance of a class. It's a specific item created using the blueprint defined by the class.

#### Creating Objects

We have seen the class definition for a `SuperHero` before.

```python
class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
```

We can create an object by calling the class and passing in the required arguments.

```python
# Creating superhero objects
iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
spider_man = SuperHero("Spider Man", "web slinging", 90, 95)
```

When we write `iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)`, we're telling Python:

1. Create a new object variable called `iron_man`

2. Use the `SuperHero` class to create it

3. Set its `name` attribute to `"Iron Man"`

4. Set its `power` attribute to `"repulsor beams"`

5. Set its `health` attribute to `100`

6. Set its `speed` attribute to `80`

#### Challenge

You have given the code for a `Pet` class. When run, this code produces an error:

```
NameError: name 'whiskers' is not defined
```

To fix this error and get the expected output, complete the following task:

- Create a pet with a name of `Whiskers`, which is a `cat` with `hunger` level 6 and `energy` level 8.

Note: The name of the variable should be `whiskers` (no uppercase).

**Expected Output:**

```
Whiskers (cat) - Hunger: 6, Energy: 8
```

Hint

- Object creation: `pet_name = Pet("Name", "species", hunger_value, energy_value)`

The importance of parameter order

When creating a new superhero object, the order of values must match the `__init__` method:

```
def __init__(self, name, power, health, speed)
```

Example:

#### Correct order

```
correct_hero = SuperHero("Captain America", "super strength", 110, 85)
```

#### Incorrect order

```
incorrect_hero = SuperHero(100, "Hulk", 75, "gamma radiation")
```

In the incorrect example, the order of attributes is mismatched. Be careful, Python won't give us any errors for this incorrect order, which means we need to be careful when creating our objects!

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
