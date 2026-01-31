# Abstraction

**🔗 [View on NeetCode](https://neetcode.io/problems/python-abstraction/question)**

---

**Abstraction** is the concept of hiding complex implementation details and showing only the necessary features to the outside world. Think of it like a TV remote - you just press buttons to change channels, not caring about the electronics inside.

**Data Abstraction**

- Hides complex data details

- In Python achieved through: private variables

**Behavioral Abstraction**

- Hides complex method implementations

- In Python achieved through: abstract methods

Let's understand abstraction through a simple example:

```python
class TempConverter:
    def __init__(self, celsius):
        self._celsius = celsius    # Hidden internal state

    def get_fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

temp = TempConverter(25)
print(temp.get_fahrenheit())  # 77.0
```

In this code:

- The `get_fahrenheit` method is the public interface that *abstracts* away the internal implementation details

- Internal variable `_celsius` is hidden from users

- Users don't need to understand the conversion formula

#### Challenge

Given the code for `Superhero` class below, create an abstraction for the `fly()` method. The user should only need to know that the superhero can fly, and not how the fly method is implemented.

Internally, the `fly()` method should check if the superhero has enough power to fly. If there power level is at least `20`, it should reduce their power level by `20` and return `"Up up and away!"`. If there power level is less than `20`, it should return `"Too tired to fly..."`.

**Expected Output:**

```
Up up and away!
Up up and away!
Too tired to fly...
```

Abstraction vs Encapsulation

Previously we discussed encapsulation. These are two distinct yet complementary concepts in object-oriented programming:

**Abstraction (hiding complexity):**

- Is about identifying essential features and hiding unnecessary details

- Focuses on WHAT an object does at a high level

- Like a TV remote - you just need to know it can change channels

- In the `TempConverter` example we discussed, the `get_fahrenheit()` method represents an abstraction because it lets users convert temperature without needing to know the formula

- Purpose: Simplifying the view of complex systems

**Encapsulation (protecting data):**

- Is about grouping data and methods that work on that data within a single unit, and restricting access to the internal data

- Controls HOW the object's data can be accessed and modified

- Like a medicine capsule - wraps and protects its contents

- In the `TempConverter` example we discussed, we encapsulate the `_celsius` variable by making it private and only allowing access through controlled methods

- Purpose: Data hiding and bundling related functionality

The key difference:

- Abstraction operates at the design level (what features to expose)

- Encapsulation operates at the implementation level (how to protect data)

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
