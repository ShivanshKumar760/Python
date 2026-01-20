# Dict Values

**🔗 [View on NeetCode](https://neetcode.io/problems/python-dict-values/question)**

---

Another way of iterating over a dictionary is by using the `values()` function. This function allows us to loop over the values in the dictionary without needing to access the keys.

```python
my_dict = {"a": 1, "b": 2, "c": 3}

for value in my_dict.values():
    print(value)
```

A useful use case for this is when we want to convert the values of a dictionary into a list. This can be done by using the `list()` function.

```python
my_dict = {"a": 1, "b": 2, "c": 3}

values = list(my_dict.values())

print(values) # Output: [1, 2, 3]
```

#### Challenge

With this in mind, once again implement the `get_dict_values(age_dict: Dict[str, int]) -> List[int]` function. It accepts a dictionary of names and ages and should return a list of the ages.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
