"""
Problem: Method Overloading
URL: https://neetcode.io/problems/python-method-overloading/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(txt1,txt2=None):
        if (txt2==None):
            return txt1.upper()
        else:
            return txt1+txt2




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
