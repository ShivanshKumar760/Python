# Diamond Problem and Method Resolution Order

**🔗 [View on NeetCode](https://neetcode.io/problems/python-diamond-problem-and-method-resolution-order/question)**

---

Multiple inheritance is a powerful but complex feature. It is very important to use multiple inheritance carefully. If used incorrectly, you can encounter situations where methods are inherited from multiple parent classes, leading to ambiguous behavior known as the **diamond problem**.

#### Understanding the Diamond Problem

Let's see an example of a diamond problem:

```python
class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("B")

class C(A):
    def print_method(self) -> None:
        print("C")

class D(B, C): 
    pass

d = D()
d.print_method()  # Which method will be called?
```

In the above code you can see that `D` is inheriting from `B` and `C`, and the `B` and `C` are inheriting from `A`. Now when you call `d.print_method()`, which method will be called? This ambiguity is known as the diamond problem.

This inheritance structure creates a diamond shape, as illustrated below:

```
A
  / \
 B   C
  \ /
   D
```

#### How Python Resolves Methods

Python uses Method Resolution Order (MRO) to determine which method to call when dealing with multiple inheritance. Here's how it works:

- First, Python looks for the method in the current class `D`

- If not found, it checks the first parent class `B` as it is the first parent class passed to the `D` class

- Then the second parent class `C` as it is the second parent class passed to the `D` class

- Finally, it checks the base class `A`

You can view this order using the `__mro__` attribute:

```python
print(D.__mro__)
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

As you can see, the MRO is `[D, B, C, A]`.

#### Challenge

Given the starter code on the right, the current MRO will print `C`. Modify the code and change the MRO to make it print `B` instead.

**Expected Output:**

```
B
```

Hint

- The order of parent classes in class D's definition determines the MRO

- Use `__mro__` to verify the method resolution order

- Try changing the order of B and C in class D's inheritance list

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
