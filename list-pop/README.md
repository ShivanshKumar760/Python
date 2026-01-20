# List Pop

**🔗 [View on NeetCode](https://neetcode.io/problems/python-list-pop/question)**

---

We can also remove elements from a list using the `pop()` function.

```python
my_list = [1, 2, 3]

my_list.pop()

print(my_list)  # Output: [1, 2]
```

By default, `pop()` removes the last element from the list. We can also specify an index to remove a specific element, as shown below.

```python
my_list = [1, 2, 3]

my_list.pop(0)

print(my_list)  # Output: [2, 3]

my_list.pop(0)

print(my_list)  # Output: [3]
```

Notice that we called `pop(0)` twice to remove the first two elements from the list. After removing the first element, the second element becomes the first element. So we call `pop(0)` again to remove the new first element.

#### Challenge

Implement the following two functions:

1. `remove_from_list(my_list: List[int], index: int) -> List[int]`. It should remove the element at the given index from `my_list` and return the modified list.

2. `pop_n_from_list(my_list: List[int], n: int) -> List[int]`. It should pop the last `n` elements from `my_list` and return the modified list.

You may assume that the index given to `remove_from_list` will always be valid (i.e., it will be within the bounds of the list). You may also assume that the number of elements to pop from the list in `pop_n_from_list` will always be less than or equal to the length of the list.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
