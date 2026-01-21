# Intro to Classes

**🔗 [View on NeetCode](https://neetcode.io/problems/python-intro-to-classes/question)**

---

Imagine you're a game developer creating a superhero game. You start by defining individual heroes:

```python
hero_1_name = "Iron Man"
hero_1_power = "repulsor beams"
hero_1_health = 100
hero_1_speed = 80

hero_2_name = "Spider Man"
hero_2_power = "web slinging"
hero_2_health = 90
hero_2_speed = 95
```

This approach has a few problems:

1. **Repetition**: You have to define each hero individually.

2. **Messy code**: It's hard to keep track of all the hero attributes and their values.

3. **Scalability**: What if you need to create 50 different heroes? Your code would become unmanageable very quickly.

#### Classes

A class is a blueprint for creating objects. Here's the basic syntax for defining a class in Python:

```python
class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
```

In Python, a class is defined with the keyword word `class` followed by the name of the class and a colon. The `__init__` method is a special method that belongs to the class. It creates an object and initializes it's attributes.

Notice that the `__init__` method has an argument `self`. This is required. The `self` variable allows us to add attributes to our object. It also prevents name conflicts, since `name` and `self.name` are different variables.

#### Challenge

Please see the starter code on the right and complete the following tasks:

1. Define a class named `Pet`.

2. Define a method for initialization: `def __init__(self, name, species)`

3. Inside the `__init__` method, initialize two attributes:

- `self.name`: assigned the value of the `name` parameter

- `self.species`: assigned the value of the `species` parameter

  
    *What is the `self` argument?*
    

In Python, `self` represents the instance of the class. It's used to access variables and methods associated with the class. When you create an object from a class, Python automatically passes the object as the first argument to the `__init__` method. You can name this argument anything you like, but `self` is the convention.

    

Don't worry if this doesn't make sense right now. We'll cover it in more detail in the upcoming lessons.

  
    *How to name classes in Python?*
    

Class names in Python use PascalCase convention, meaning each word starts with a capital letter and there are no underscores between words (e.g., SuperHero, IronMan, SpiderMan).

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
