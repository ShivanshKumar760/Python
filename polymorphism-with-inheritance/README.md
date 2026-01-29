# Polymorphism with Inheritance

**🔗 [View on NeetCode](https://neetcode.io/problems/python-polymorphism-with-inheritance/question)**

---

**Polymorphism** means "many forms" in Greek. In programming, it lets objects behave differently while sharing a common interface. An analogy would be different phones being able to charge with the same charger.

#### Runtime Polymorphism

- Decided during program execution

- In Python it can be achieved through Method Overriding and Duck Typing

Let's understand Runtime Polymorphism through Method Overriding:

```python
class Superhero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
    
    def special_power(self) -> None:
        pass # Not needed for this example

class IronMan(Superhero):
    def special_power(self) -> None:
        print(f"{self.name} uses {self.power}")

class Thor(Superhero):
    def special_power(self) -> None:
        print(f"{self.name} uses {self.power}")
```

Above we have a class `Superhero` and two subclasses `IronMan` and `Thor`.

```python
def display_power(hero: Superhero) -> None:
    hero.special_power()

iron_man = IronMan("Iron Man", "repulsor beams")
thor = Thor("Thor", "hammer")

display_power(iron_man)  # Iron Man uses repulsor beams
display_power(thor)      # Thor uses hammer
```

Above we have a function `display_power` that takes an object of type `Superhero` and calls its `special_power` method. It accepts any object of type `Superhero` (or its subclasses) and calls their `special_power` method.

We pass in an instance of `IronMan` and an instance of `Thor` to the `display_power` function and it calls the correct `special_power` method for each instance.

This works because we expect a `Superhero` object and any subclass of `Superhero` will have a `special_power` method, even if it has not been overridden.

#### Compile-time Polymorphism

- Decided at compilation time (before the code starts running)

- In Python it can be achieved through method overloading

#### Challenge

Look at the code for the `Animal` class below and complete the following tasks:

- Create a `Dog` class that inherits from the `Animal` class and overrides the `make_sound` method to print `"[name] says: Woof!"`.

- Create a `Cat` class that inherits from the `Animal` class and overrides the `make_sound` method to print `"[name] says: Meow!"`.

- Create a function that accepts any object of type `Animal` and calls their `make_sound` method.

**Expected Output:**

```
Animal is making a sound
Buddy says: Woof!
Whiskers says: Meow!
```

Hints

- Remember to use inheritance syntax: `ChildClass(ParentClass)`

- Remember to use the common interface parameter: `parent: ParentClass`

- Remember to call make_sound: `parent.make_sound()`

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
