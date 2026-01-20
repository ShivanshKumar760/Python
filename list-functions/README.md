# List Functions

**🔗 [View on NeetCode](https://neetcode.io/problems/python-list-functions/question)**

---

Python also provides some built in functions to get the sum, minimum, and maximum of a list:

```python
my_list = [1, 2, 3, 4, 5]

print(sum(my_list))  # Output: 15
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 5
```

1. The `sum()` function returns the sum of all the elements in the list.

2. The `min()` function returns the smallest element in the list.

3. The `max()` function returns the largest element in the list.

#### Challenge

Implement the following functions on the right:

1. `get_sum(my_list: List[int]) -> int` should return the sum of all the elements in the list.

2. `get_min(my_list: List[int]) -> int` should return the smallest element in the list.

3. `get_max(my_list: List[int]) -> int` should return the largest element in the list.

You may assume the list passed in will always have at least one element.

If you want a challenge, try to implement these functions *without* using the built-in `sum()`, `min()`, and `max()` functions. Instead, you can use a loop to iterate through the list and keep track of the sum, minimum, and maximum.

*Hint*: It's generally not wise to name variables `sum`, `min`, or `max` since these are built-in functions. If you do, you will overwrite the built-in functions and won't be able to use them anymore.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
