# Class Attributes

**🔗 [View on NeetCode](https://neetcode.io/problems/python-class-attributes/question)**

---

When assembling the Avengers to fight Thanos, certain information needs to be shared across all heroes. For instance, Nick Fury needs to track how many heroes we have ready for battle. This is where **class attributes** come in.

```python
class Superhero:
    hero_count = 0      # Class attribute
    
    def __init__(self, name: str, power: str):
        self.name = name      # Instance attribute
        self.power = power    # Instance attribute
        Superhero.hero_count += 1
```

In the above code, `hero_count` is a class attribute, where as `name` and `power` are instance attributes.

In this case, `hero_count` belongs to the entire superhero class - not to individual heroes. This attribute is shared by all instances of the class. Unlike instance attributes, we don't use the `self` keyword to access class attributes.

Class attributes must be declared *outside* the `__init__` method and without the `self` keyword.

```python
iron_man = Superhero("Iron Man", "repulsor beams")
thor = Superhero("Thor", "lightning")

print(f"Heroes ready to face Thanos: {Superhero.hero_count}")  # This should print 2
```

In the above code, we created two instances of the `Superhero` class, `iron_man` and `thor`. We then accessed the class attribute `hero_count` using the class name `Superhero.hero_count`.

Notice that we access class attributes using the class name, not the instance name. This is because class attributes are shared by all instances of the class. Class attributes can be updated outside the class as well.

**Note:** We can also access the class attribute using the instance of the class `iron_man.hero_count` but it's not recommended. That's because the class attribute belongs to the class, not to the instance.

#### Challenge

You are given code for class `SmartDevice`. Modify it to track the total and active devices in your house:

1. Add two class attributes:

- `total_devices`: Track total number of devices created, initialized to `0`

- `active_devices`: Track number of devices currently turned on, initialized to `0`

1. Implement these methods:

- `turn_on()`: Increase active devices by 1

- `turn_off()`: Decrease active devices by 1

Note:

- `total_devices` increases in `__init__` (already done for you)

- Methods should only update `active_devices` count

**Expected Output**

```
Total Devices: 2
Active Devices: 1
```

Hints

- Use `className.attributeName = value` to update the class attribute

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
