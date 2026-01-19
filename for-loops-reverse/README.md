# For Loops Reverse

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-for-loops-reverse/question)

---

## 📋 Problem Description

We can also use a for loop to iterate through a sequence of numbers in reverse order. To do this, we can pass a negative number as the third parameter to the range() function. This number will be the step, and it will determine how much the variable will decrement by on each iteration of the loop.

The above two loops are equivalent. Each loop will print the numbers 10 through 1. The 10 passed into the range() function is the starting number.

The 0 passed into the range() function is the ending number. The loop will stop once it reaches or is less than this number. Meaning that the number 0 is not included in the sequence.

The -1 passed into the range() function is the step. This is how much the variable will decrement by on each iteration of the loop. ChallengeUsing a for loop, print the numbers 20 through 10, in reverse order, including 20 and 10. A shortcut for reverse order. There is a shortcut in Python for iterating through a sequence in reverse order. You can use the function reversed() to reverse a sequence. for i in range(10): will iterate from 0 to 9. for i in reversed(range(10)): will iterate from 9 to 0.

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
