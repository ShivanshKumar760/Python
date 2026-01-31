# Abstract Method and Class

**🔗 [View on NeetCode](https://neetcode.io/problems/python-abstract-method-and-class/question)**

---

So far we have seen the general concept of abstraction. Now let's explore two key concepts which are used to achieve abstraction in Python.

1. An **abstract method** is a method that is declared in a base class, but contains no implementation. The child class must implement the abstract method. Abstract methods are used to enforce a contract on subclasses. Subclasses must implement the abstract method, otherwise they will raise an error.

2. An **abstract class** is a class that contains one or more abstract methods. It serves as a blueprint for other classes and cannot be instantiated on its own.

Let's look at an example.

```python
from abc import ABC, abstractmethod

class Superhero(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str: # public methods
        return self._name

    @abstractmethod
    def fly(self) -> str:
        pass

class Superman(Superhero):
    def fly(self) -> str:
        return "Up up and away!"
```

In the above example:

- `Superhero` is the base abstract class that inherits from `ABC`. In python, abstract classes are created by inheriting from `ABC`.

- The `@abstractmethod` decorator marks `fly()` as an abstract method. In python, abstract methods are created by decorating a method with `@abstractmethod` decorator.

- `Superman`, and any other child class that inherits from `Superhero`, must implement the `fly()` method.

- Non-abstract methods like `get_name()` are optional to override.

Note you can't create an instance of `Superhero` class because it is an abstract class and has an abstract method.

```python
hero = Superhero("Superman")
```

This will raise a `TypeError` because the `fly()` method is not implemented.

#### Why use abstract method?

Abstract methods are a powerful tool for achieving abstraction because they:

1. Hide implementation details (abstraction): The base class only declares what methods must exist, without specifying how they work.

2. Enforce consistency: Child classes must implement these methods, ensuring a standard interface across all subclasses, which allows for polymorphism.

3. Prevent incomplete objects: You can't create instances of classes with abstract methods, ensuring only fully-implemented classes can be used.

#### Challenge

In this challenge, you'll implement a payment card system using abstract classes. You are given a class `PaymentCard`.

Your tasks are:

1. Make the `PaymentCard` class abstract.

2. Add an abstract method `process_payment` to the `PaymentCard` class which takes a float `amount` as an argument and returns a string.

3. Implement a `DebitCard` class that:

- Inherits from `PaymentCard`

- Implements the `process_payment` method. It should take an `amount` as an argument and subtract it from the balance. If the balance is less than the amount, it should return `"Insufficient funds"`. Otherwise, it should return `"Payment successful"` and update the balance.

4. Implement a `CreditCard` class that:

- Inherits from `PaymentCard`

- Implements the `process_payment` method. It should take an `amount` as an argument and subtract it from the balance. It should always approve payments (negative balance is allowed).

#### Expected Output

```
Payment successful
50.0
Insufficient funds
50.0
Payment successful
50.0
Payment successful
-50.0
```

Hints

- Use the `ABC` class from the `abc` module to define the `PaymentCard` class as an abstract class.

- Use the `abstractmethod` decorator from the `abc` module to define the `process_payment` method as an abstract method.

- As the `PaymentCard` class is abstract, you can implement the `process_payment` method as a concrete method.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
