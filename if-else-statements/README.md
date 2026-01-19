# If-Else Statements

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-if-else/question)

---

## 📋 Problem Description

It's common to want to run a separate piece of code when an if statement fails to execute. For example:

The above code will print "Account is in good standing." because the balance is greater than or equal to 0. The first if statement will not execute because the condition is False. But we can rewrite this code using an else statement:

This code is mostly equivalent to the first example. But the else block only executes if previous if statement fails to execute. We cannot have an else statement without an if statement preceding it. Conditional statements like if and else can also be used to add multiple return statements within the same function as shown below.

The function above will return the maximum of two numbers. If a is greater than b, the function will return a. Otherwise, it will return b. Once a return statement is executed, the function will stop executing.

ChallengeUsing this knowledge, implement the get_min(a: int, b: int) -> int function in the code editor. It should return the minimum of a and b. If they are equal, it doesn't matter which value you return.

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
