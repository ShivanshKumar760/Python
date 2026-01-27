# Method Overriding

**🔗 [View on NeetCode](https://neetcode.io/problems/python-method-overriding/question)**

---

So far, we have seen how to inherit properties and methods from a parent class. But what if we want to change the behavior of a method in a child class? This is where method overriding comes in.

Method overriding allows us to change the behavior of a method in a child class. This is useful when we want to change the behavior of a method that is inherited from a parent class.

Let's see an example:

```python
class Superhero:
    def __init__(self, name: str):
        self.name = name

    def fight(self) -> None:
        print("Superhero fights with advanced weapons!")

class Avenger(Superhero):
    # Override the fight method
    def fight(self) -> None:
        print("Avenger fights with advanced weapons!")
```

In this example, we have a `Superhero` class with a `fight` method. We then have a `Avenger` class that inherits from the `Superhero` class. The `Avenger` class has its own `fight` method that overrides the `fight` method in the `Superhero` class.

```python
avenger = Avenger("Iron Man")
avenger.fight() # Output: Avenger fights with advanced weapons!
```

Above, we create an instance of the `Avenger` class and call the `fight` method. The `fight` method in the `Avenger` class is called instead of the `fight` method in the `Superhero` class.

The method from the child class is called instead of the method from the parent class. This is method overriding.

#### Challenge

You are given the code for an `Animal` class. Your tasks are:

1. Create a `Dog` class and a `Cat` class that inherit from the `Animal` class.

2. Override the `make_sound` method in the `Dog` class to make the dog bark. Use the print statement `print(f"{self.name} is barking")`.

3. Override the `make_sound` method in the `Cat` class to make the cat meow. Use the print statement `print(f"{self.name} is meowing")`.

**Expected Output:**

```
Animal makes a sound
Max is barking
Luna is meowing
```

Hint

- Remember the synntax for class inheritance.

```python
class ChildClass(ParentClass):
    # Child class code here
```

- Remember the synntax for method overriding.

```python
class ChildClass(ParentClass):
    def method_name(self):
        # Child class code here
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
