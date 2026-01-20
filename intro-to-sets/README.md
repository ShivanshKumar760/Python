# Intro to Sets

**🔗 [View on NeetCode](https://neetcode.io/problems/python-intro-to-sets/question)**

---

In Python, a **set** is very similar to a list, but with a few key differences.

- A set is *unordered*, meaning the elements are not stored in a specific order. If order is important, you should use a list.

- A set can only contain *unique* elements. If you try to add a duplicate element to a set, it will be ignored.

Here is an example:

```python
my_set = {1, 2, 3}

print(my_set)  # Output: {1, 2, 3}

my_set = {3, 2, 1}

print(my_set)  # Output: {1, 2, 3}
```

As you can see, a set can be created using curly braces `{}` with elements separated by commas. When printing a set, the elements sometimes appear in sorted order, but this is *not* guaranteed. A `set` makes no gurantees about the order of the elements stored.

```python
my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(1)

print(my_set)  # Output: {1, 2}
```

Above we declared an empty set with `set()`. We then added the elements `1` and `2` to the set. When we tried to add `1` again, it was ignored because it was already in the set. This is because sets can *not* contain duplicate elements.

  
    *Why can't we declare an empty set with curly braces?*
    

If we used empty curly braces `{}`, it would **not** have declared a set. That's because Python uses curly braces to declare an empty dictionary. A dictionary is a data structure that stores key-value pairs. We will learn more about dictionaries soon.

#### Challenge

Implement the function `list_to_set(nums: List[int]) -> Set[int]`. It should take a list of integers and return a set containing the unique elements from the list. The order the elements appear in the set does not matter.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
