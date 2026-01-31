# Interface

**🔗 [View on NeetCode](https://neetcode.io/problems/python-interface/question)**

---

An **interface** in Python is just like an abstract class, but with one key difference: it contains only abstract methods. While abstract classes can mix both concrete and abstract methods, an interface is a "pure" abstract class. It only defines a contract of what methods must be implemented.

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def query(self, sql: str) -> list:
        pass
```

This is an interface because it contains only abstract methods `connect` and `query` - it serves as a pure contract that specifies what methods implementing classes must provide. While some programming languages have dedicated `interface` keywords, Python achieves the same functionality using abstract classes (`ABC`).

#### Interfaces vs Abstract Classes

Key differences between interfaces and abstract classes in Python:

1. Interfaces contain only abstract methods (pure contract)

2. Abstract classes can mix both concrete and abstract methods

3. Abstract classes can have constructors (`__init__`), While Python allows `__init__` methods in interfaces, it's considered bad practice as interfaces should focus purely on method contracts

#### Challenge: Create a Superhero Interface

You are given the code for `Superman` and `WonderWoman` classes. Both are inheriting from the `Superhero` which hasn't been defined yet. You task is to:

1. Create a `Superhero` interface.

2. In the `Superhero` interface, define the `abstract` methods `fly` and `use_power`

#### Expected output

```python
True
True
```

Hints

- Ensure that the `Superhero` interface is inheriting from the `ABC` class

- Every abstract method should be decorated with the `@abstractmethod` decorator

- Use `from abc import ABC, abstractmethod` to import the `ABC` and `abstractmethod` classes

- Remember interface doesn't have a constructor `__init__` method.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
