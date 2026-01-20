# Reading Input

**🔗 [View on NeetCode](https://neetcode.io/problems/python-read-input/question)**

---

So far we have only printed output to the console, but what if we want to take input from the console?

In Python, the `input()` function is used to read input to the program while the program is running. This input comes from a stream of data called *standard input* or *stdin*. This can either mean the data a user types in manually into the terminal (console) or input that is supplied to the program before it is run.

In this course, we will be directly supplying input to your program to simulate user input.

```python
user_input = input("Enter some text: ") 

print(user_input) # This will print the input to the console
```

In the above code, `input()` will print the *string* `"Enter some text: "` to the console and read one line of input from stdin. The input will be in the form of a *string* and will be stored in the variable `user_input`.

When `input()` prints text, the following print statement will be on the same line as the prompt. So if the input was `"some text"` in the above example, the output would be:

```plaintext
Enter some text: some text
```

#### Challenge

Implement a function called `read_and_print_input() -> None`. It should read a single line of input from the console and print it to the console. The prompt it should provide is `"Reading one line of text into a string: "`. Note that there is a space after the colon.

Call your function exactly `2` times.

  
    *Why doesn't input print on a different line?*
    

There is a special character in programming called the newline character `\n`. This character is used to move the cursor to the next line, similar to how you would press the Enter key on your keyboard.

    

Even though it's called the "newline" character, it's actually two characters: a backslash `\` and the letter `n`. When you see `\n` in a string, it tells Python to move to the next line.

    

By default, Python adds a newline character to the end of the string when it calls `print()` to the console.

    

The `input()` function does **not** do this. It prints to the console without a newline character, so the next print statement will be on the same line.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
