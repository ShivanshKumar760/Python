# Printing Text

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-printing-text/question)

---

## 📋 Problem Description

Earlier we printed Hello, world! to the console. You may have noticed that we used double quotes "" around the text. This is known as a string in programming. Most languages use double quotes to define a string.

Some languages like Python (and JavaScript) also allow you to use single quotes '' to define a string.

A string is just a sequence of characters between the opening and closing quotes. But what if we wanted to print a string that also contains quote characters? For example, how would the Python interpreter know where the following string ends?

This code will cause an error. Python thinks we have a string "They said, ", followed by Hello, world!, which is outside of the quotes (not apart of the string).

One possible solution to this is to use a backslash \, aka the escape character, before each quote character inside the string.

This tells Python we want to interpret the quote " as a character inside the string, not as a quote that ends the string.

ChallengeYour task is to correct the code in the code editor to print the following text to the console:

If you think you have the correct answer, click the Submit button. Is there another solution? Yes! Another way to define a string is to use single quotes instead of double quotes. So alternatively, if we want to use double quotes inside of a string, we can define the string using single quotes. print('They said, "Hello, world!"') This way we don't need to use the escape character. The choice between single and double quotes is up to you. The first solution we discussed is useful because it works in more programming languages, since not all languages allow you to use single quotes to define a string. By the way, we can also use single quotes inside of double quotes without any issues. print("They said, 'Hello, world!'")

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
