# Parse Input

**🔗 [View on NeetCode](https://neetcode.io/problems/python-parse-input/question)**

---

Sometimes we have to do more than just convert the input to a single type. We might need to restructure the input in some way. This is called **parsing** the input.

Suppose you read a list of integers separated by commas into a string, but you want to store them as a list. You can use the `split()` method to split the string by commas. This will convert "1,2,3" into a list of strings `["1", "2", "3"]`.

```python
number_string = "1,2,3"

string_list = number_string.split(",")

print(string_list) # Output: ['1', '2', '3']
```

The above code will split the numbers by the `","` substring, and store each number as a string in the list `string_list`, which is a list of strings. In this case, the `","` is considered the **delimiter**.

#### Challenge

Implement the `read_integers() -> List[int]` function. It should read a line from stdin, without printing anything, and return a list of integers. You may assume every line will be in the following format, where the numbers are separated by commas:

```plaintext
1,2,3,4,5
```

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
