# Global vs Local Scope

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-global-vs-local/question)

---

## 📋 Problem Description

Here are a few more examples illustrating scope in Python:

In the code above, the variable inside_function_only is declared inside the function declare_variable. This variable has a local scope and is only accessible within the function. Attempting to access it outside the function will result in a NameError.

In the code above, the variable n is declared outside the function print_global_variable. This variable has a global scope, since it's not within a function, and can be accessed from anywhere in the program, including inside functions. Note: We saw earlier, that if the function has a parameter with the same name as a global variable, the function will use the local variable instead of the global variable.

Global Scope: Variables declared outside of any function have a global scope.

They can be accessed from anywhere in the program, including inside functions. Local Scope: Variables declared within a function have a local scope.

They can only be accessed within the function in which they are defined.

Local variables are created when the function is called and destroyed when the function exits. ChallengeThere's a bug in the code on the right, if you try to run it you'll see a NameError. Can you fix it so that the output is:

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
