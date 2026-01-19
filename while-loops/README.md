# While Loops

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-while-loops/question)

---

## 📋 Problem Description

What if we really love Python and we want to print so 5 times:

The above code is sufficient. But is there a better way? Yes! We can use a while loop.

Pay close attention to each line above. It's kind of like a repeating if statement. The code block under the while statement will run zero or more times, as long as the condition i < 5 is True. The i += 1 line is important because it increments the value of i by 1 each time the code block runs. If we didn't have this line, the loop would run forever! The variable i starts at 0, then is 1, then 2, then 3, then 4. When i is 5, the condition i < 5 is no longer True, so the loop stops. The loop is executed 5 times.

Also note that just like with if statements, whitespace matters. Make sure the code that belongs to the loops is indented.

ChallengeIn the code editor, use a loop to print "I know how to use while loops" exactly 12 times. What is the scope of a while loop? The scope of a while loop is the same as an if statement, so just like if statements, loops do not create their own scope. All variables declared within the while loop are accessible outside of the loop. Loops share the same scope as the function they are in. Or the global scope if they are not in a function.

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
