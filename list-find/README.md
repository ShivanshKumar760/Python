# List Find

**🔗 [View on NeetCode](https://neetcode.io/problems/python-list-find/question)**

---

We learned that we can determine if a list contains a specific element with the `in` operator. We can also find the index of an element in a list using the `index()` function.

```python
my_list = [1, 2, 3, 4, 5, 3]

print(my_list.index(3))  # Output: 2
```

The above code snippet will print the index of the first occurence of the element `3` in the list `my_list`. There are two `3`s in the list, but the first one is at index `2`, so `2` is printed. If the element is not present in the list, a `ValueError` will be raised.

#### Challenge

Implement the `find_index(nums: List[int], target: int) -> int` function. It should return the index of the first occurrence of the target number in the list. You may assume that the target number will always be present in the list.

If you want a challenge, try to implement the function without using the built-in `index()` method.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
