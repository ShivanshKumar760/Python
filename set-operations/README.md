# Set Operations

**🔗 [View on NeetCode](https://neetcode.io/problems/python-set-operations/question)**

---

We can also perform various operations on sets in Python. We can remove elements from a set using the `remove()` function. If the element is not present in the set, a `KeyError` will be raised.

```python
my_set = {1, 2, 3}

my_set.remove(2)

print(my_set)  # Output: {1, 3}

my_set.remove(4)  # Raises KeyError
```

Just like with lists, we can loop over elements within a set using `for` loops. The difference is that we can't access elements by index because sets are unordered. The order that we loop over a set is not guaranteed.

```python
my_set = {1, 2, 3}

for element in my_set:
    print(element)
```

We can also convert a list into a set by passing the list into the `set()` function. We can then convert the set back into a list by passing it into the `list()` function. This is an easy way to remove duplicates from a list.

```python
my_list = [1, 2, 3, 4, 5, 1, 2, 5]

my_set = set(my_list)

print(my_set)  # Output: {1, 2, 3, 4, 5}

my_list_no_duplicates = list(my_set)
```

Just like with lists, we can also use the `in` keyword to check if an element is present in a set.

```python
my_set = {"Cat", "Dog", "Mouse"}

contains_cat = "Cat" in my_set   # True
contains_lion = "Lion" in my_set # False
```

#### Challenge

Implement the function `count_unique_words(words: List[str]) -> int` which accepts a list of strings `words` and returns the number of unique words in the list. It's possible the list may be empty, in which case the function should return 0.

*Hint*: You can call the `len()` function on a set to get the number of elements in the set.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
