# Dict Remove

**🔗 [View on NeetCode](https://neetcode.io/problems/python-dict-remove/question)**

---

You can remove an item from a dictionary using the `pop()` function. This function takes a key as an argument and removes the key-value pair from the dictionary. If the key doesn't exist, it will raise a `KeyError`.

```python
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict.pop("a")

print(my_dict) # Output: {"b": 2, "c": 3}

my_dict.pop("d") # Raises KeyError
```

If you don't want to worry about handling the `KeyError`, you can use the second argument of the `pop()` function. This argument is the default value that will be returned if the key doesn't exist.

```python
my_dict = {"a": 1, "b": 2, "c": 3}

value = my_dict.pop("d", 0) # Returns 0, no error occurs
```

You can also use the `del` keyword to remove a key-value pair from a dictionary. This is a bit more concise than using the `pop()` function.

```python
my_dict = {"a": 1, "b": 2, "c": 3}

del my_dict["a"]
```

#### Challenge

Implement the `remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]` function. It accepts a dictionary `my_dict` and a list of strings `keys`. The function should remove all the keys in the list from the dictionary and return the modified dictionary. If a key doesn't exist in the dictionary, ignore it.

*Be careful*: If you try to remove a key that doesn't exist, it will raise a `KeyError`. Make sure to handle this case by checking if the key exists before trying to remove it, or using the second argument of the `pop()` function.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
