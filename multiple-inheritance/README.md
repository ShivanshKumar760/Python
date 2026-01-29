# Multiple Inheritance

**🔗 [View on NeetCode](https://neetcode.io/problems/python-multiple-inheritance/question)**

---

Multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. While powerful, it is generally considered an anti-pattern.

Let's see an example:

```python
class Swimmer:
    def swim(self):
        print("Swimming")

class Flyer:
    def fly(self):
        print("Flying")

# Ducks inherits from both Swimmer and Flyer
class Duck(Swimmer, Flyer):  
    pass
```

In this example, the `Duck` class inherits from both the `Swimmer` and `Flyer` classes. This means that a `Duck` object will have access to both the `swim` and `fly` methods. The names of the parent classes are passed as arguments to the `Duck` class. Currently, we are only using the methods from the parent classes so we just use the `pass` keyword to indicate that we are not adding any new methods or attributes to the `Duck` class.

Below, we create an instance of the `Duck` class and call the `swim` and `fly` methods.

```python
duck = Duck() 
duck.swim() # Should print "Swimming"
duck.fly()  # Should print "Flying"
```

Be careful with multiple inheritance. It can be useful in scenarios where a class needs to inherit behavior from multiple sources. However, it can also lead to complex class hierarchies, and it's important to ensure that the inheritance is logical and avoids conflicts.

In most cases, you should *not* use multiple inheritance. But you may see code like this in the wild.

#### Basic Syntax

```python
class ChildClass(ParentClass1, ParentClass2, ...):
    # Class body
```

#### Challenge

You are given the code for `ElectronicDevice` and `HealthDevice` classes. Your task is to create a `SmartWatch` class that inherits from both `ElectronicDevice` and `HealthDevice`. Use the `pass` keyword to indicate that we are not adding any new methods or attributes to the `SmartWatch` class.

**Expected Output:**

```
Device is turning on
Measuring heart rate
Device is turning off
```

Hint

To create a class that inherits from multiple parent classes, you can pass the parent classes as arguments to the child class.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
