# Control Flow

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-control-flow/question)

---

## 📋 Problem Description

Python provides control statements to alter the execution of loops. break: Exits the loop immediately.

continue: Skips the remaining code inside the loop for the current iteration and moves to the next iteration.

pass: Acts as a placeholder and does nothing. We cannot have empty loops, so we use pass to avoid errors. It can also be used in conditional statements and functions. Here's an example demonstrating pass:

None of the above code will actually do anything, but it also won't cause an error.

Here's an example demonstrating the break and continue control statements:

The output would be:

Notice that the output is missing some numbers? Thats because when i was equal to 3 the if statements block of code executed causing the loop to continue to the next iteration of the loop, before reaching the print(i) line. When number was equal to 6 the loop exited, because the break statement executed.

For the numbers where neither condition executed, the print(i) line was reached.

Control flow statements are commonly used, but they are not usually required. They are generally used to make code more readable.

ChallengeSubmit the code on the right to prove that it will not cause any error, and also not do anything.

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
