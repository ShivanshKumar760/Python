# Inheritance Basics

**🔗 [View on NeetCode](https://neetcode.io/problems/python-inheritance-basics/question)**

---

**Inheritance** is a fundamental concept in object-oriented programming that allows you to create a new class based on an existing class. The new class, known as the **child class** or **subclass**, inherits properties and methods from the existing class, known as the **parent class** or **superclass**.

Inheritance allows us to create new classes based on existing ones. Instead of modifying an existing class, inheritance lets us reuse its code while only writing the differences we need in the new class.

#### Example

For example, let's say we have a class `Superhero`.

```python
class Superhero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
```

Now we want to create a new class `Avenger` that is a modified version of the `Superhero` class. The `Avenger` class will have the same properties and methods as the `Superhero` class, but we can also add a new method `fly` that is specific to the `Avenger` class.

```python
class Avenger(Superhero):
    def fly(self) -> None:
        print(f"{self.name} can fly using {self.power}")

iron_man = Avenger("Iron Man", "repulsor beams")
iron_man.fly() # Iron Man can fly using repulsor beams
```

In this example, the `Avenger` class inherits from the `Superhero` class. The `Avenger` class has all the properties `name` and `power` from the `Superhero` class, plus the `fly` method, even though we didn't define them in the `Avenger` class.

The syntax for inheriting from a class is as follows:

```python
class ChildClass(ParentClass):
    # Child class code here
```

When an instance of a child class is created, the constructor of the parent class is called automatically. This is why we can pass the arguments `name` and `power` to the `Avenger` class constructor, even though they are not defined in the `Avenger` class.

#### Challenge

Let's take the parent class `SmartDevice` with property `name`. Your task is to create a child class `SmartLight` that inherits from the `SmartDevice` class and has a method `turn_on` and `turn_off`.

- `turn_on` method should print `{self.name} is turned on`

- `turn_off` method should print `{self.name} is turned off`

**Expected Output**

```
Smart Light is turned on
Smart Light is turned off
```

Hints

- use the `ChildClass(ParentClass)` syntax to inherit from the parent class

Why create child classes and not an object?

You may wonder that we could just create an object of the class and add specific properties and methods instead of creating a child class. Like in our example, we could just add a property `type` to the `Superhero` class instead of creating a child class. Let's see why this could be a problem:

```python
# Without inheritance - One big messy method
class Superhero:
   def fight(self) -> None:
       if self.type == "avenger":
           print(f"{self.name} fights with advanced weapons!")
       elif self.type == "street":
           print(f"{self.name} fights with martial arts!")
       elif self.type == "magic":
           print(f"{self.name} fights with spells!")
       # More types = More if-elif statements...

# With inheritance - Clean and organized
class Avenger(Superhero):
   def fight(self) -> None:
       print(f"{self.name} fights with advanced weapons!")

class StreetHero(Superhero):
   def fight(self) -> None:
       print(f"{self.name} fights with martial arts!")
```

When each hero type fights differently, inheritance keeps the code clean by giving each type its own fight method, instead of using lots of if-elif statements.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
