# Object Attributes

**🔗 [View on NeetCode](https://neetcode.io/problems/python-object-attributes/question)**

---

**Attributes** are the properties that define or belong to an object. In our superhero example, we have the following attributes for a superhero: `name`, `power`, `health`, and `speed`.

#### Accessing Attributes

To access an object's attributes, we use dot notation: `object_name.attribute_name`. Let's create a superhero and access its attributes:

```python
class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)

print(iron_man.name)    # Iron Man
print(iron_man.power)   # repulsor beams
```

#### Modifying Attributes

We can also *modify* an attribute's value using the same dot notation:

```python
iron_man.health = 90
iron_man.power = "advanced repulsor technology"

print(iron_man.health)  # 90
print(iron_man.power)   # advanced repulsor technology
```

#### Attribute Types

While Python won't give us any errors when changing the data type of an attribute, we should avoid doing so to avoid unexpected behavior.

```python
iron_man.name = 42       # Allowed but bad practice
iron_man.health = "full" # Allowed but bad practice
```

#### Challenge

You are given a `Pet` class and an object from that class `whiskers`.

1. Print the attributes of `whiskers` with the formatting below.

2. *Decrease* the `hunger` attribute by 3, and *increase* the `energy` attribute by 2.

3. Print the attributes of `whiskers` again with the formatting below.

Expected Output:

```
Initial Attributes: Whiskers (cat) - Hunger: 6, Energy: 8
Modified Attributes: Whiskers (cat) - Hunger: 3, Energy: 10
```

Hints

- Access: `pet_object.attribute`

- Modify: `pet_object.attribute = new_value` or `pet_object.attribute += value`

- Print: `f"Attributes: {pet_object.name} ({pet_object.species}) - Hunger: {pet_object.hunger}, Energy: {pet_object.energy}"`

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
