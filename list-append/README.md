# List Append

**🔗 [View on NeetCode](https://neetcode.io/problems/python-list-append/question)**

---

We can do more than just change individual elements within a list. We can also add new elements to the end of a list using the `append()` function.

```python
my_list = [1, 2, 3]

print(my_list)  # Output: [1, 2, 3]

my_list.append(4)

print(my_list)  # Output: [1, 2, 3, 4]
```

A few things to notice:

1. We can print an entire list at once.

2. The `append()` function adds an element to the end of the list. This is not a separate function, it's called with a period after the list name (`.append()`). This is called a **method**. It is a function that is associated with a specific object (in this case, a list is an object).

3. After calling append, the original list has been *modified* to include the new element at the end. The length increased from `3` to `4`.

#### Challenge

Implement a function called `append_to_list(my_list: List[int], elements: List[int]) -> List[int]`. It should append each number from `elements` to the end of `my_list` and return the modified list.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
