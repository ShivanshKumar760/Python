# Duck Typing

**🔗 [View on NeetCode](https://neetcode.io/problems/python-duck-typing/question)**

---

**Duck Typing** is a polymorphism concept where the type of an object is determined by its behavior rather than its explicit declaration. In other words, if an object has the methods or attributes that are required by a function or method, it can be used in that context, regardless of its actual class or type.

The name **Duck Typing** comes from the phrase "If it walks like a duck and quacks like a duck, then it's a duck!"

```python
class IronMan:
    def attack(self) -> str:
        return "Repulsor Blast!"

class Thor:
    def attack(self) -> str:
        return "Lightning Strike!"

def hero_attack(hero) -> None:
    print(hero.attack())

# Create heroes and attack!
iron_man = IronMan()
thor = Thor()

hero_attack(iron_man)  # Repulsor Blast!
hero_attack(thor)      # Lightning Strike!
```

We can see that `hero_attack` doesn't check the type of the object, it only checks if the object has the `attack` method.

This is not possible in languages like Java or C++. In those languages, we need to declare the type of the object and then use it. Python makes this possible because it is a dynamically typed language.

#### Why use Duck Typing?

- **Flexibility:** We don't need `IronMan` or `Thor` to inherit from a `Superhero` class. Any new hero class that has an `attack()` method will work with `hero_attack()!`

- **Less Code:** No parent classes, no inheritance syntax. Just create classes with the methods you need.

- **Loose Coupling:** `IronMan` doesn't need to know `Thor` exists, and neither needs to know about a `Superhero` parent class. They just need their `attack()` method!

While Duck typing is powerful, it can also be error prone. We may accidentally call a method that doesn't exist on the object.

#### Challenge

You are given the `SpiderMan` class below.

1. Create a `BlackWidow` class with:

- An `attack()` method that returns `"Widow's Bite!"`

- A `defend()` method that returns `"Acrobatic Dodge!"`

2. Create a `battle_sequence()` function that:

- Takes an object as a parameter

- First it should call the `attack()` method and print the result

- Then it should call the `defend()` method and print the result

#### Expected output:

```markdown
Web Shooter!
Spider Sense!
Widow's Bite!
Acrobatic Dodge!
```

Hints

- Use the `print(hero.attack())` and `print(hero.defend())` to print the result inside the `battle_sequence()` function

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
