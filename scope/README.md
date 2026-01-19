# Scope

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-scope/question)

---

## 📋 Problem Description

Consider the following code: First n is assigned the value of 10 and printed. Next we call the function print_number and pass in the value 11. The name of the parameter for this function is also n. But this does not cause an error in Python. After the function call is complete, the value of the original n is printed and it's still 10. This can be explained by the concept of scope in programming.

In programming, the scope refers to the visibility or accessibility of variables within different parts of the code. The value 11 passed into the print_number() function, is only accessible within the function. The function has its own scope, and the variable n inside the function is a different variable than the one outside the function. This is why the value of the original n is still 10 after the function call. ChallengeTo prove that the variable n inside the function is different than the one outside, consider this code:

What do you think the output of the last print statement will be? Will it be 10 or 11? Run the code in the editor to find out. Wait why? The value of the variable n outside the function remains unchanged because the variable n inside the function is a different variable, even though they share the same name. When we pass the value of n into the function, the function creates a new copy of n that is local to the function (only accessible within the function). Any changes made to this local variable do not affect the original variable outside the function.

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
