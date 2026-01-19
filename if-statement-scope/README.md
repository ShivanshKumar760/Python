# If Statement Scope

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-if-scope/question)

---

## 📋 Problem Description

Unlike functions, if statements do not create a new scope. This means that variables defined inside an if statement are accessible outside of the if statement. Here's an example:

They can also update variables that were defined outside of the if statement. Here's an example:

Within functions, if statements have the same scope as the function. This means that variables defined inside an if statement are accessible within that function, but not outside of it. Here's an example:

ChallengeIn the code editor, implement the pay_bill(balance: int, bill: int) -> int function. It accepts two parameters, balance and bill, where balance is the current account balance and bill is the amount of the bill that needs to be paid.

If the balance is greater than or equal to the bill, the function should return the new balance after subtracting the bill from the balance. Otherwise, the function should return the balance without making any changes.

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
