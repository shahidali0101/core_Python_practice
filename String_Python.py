# Python_Strings_Manipulation.py
"""
Topic: Strings in Python & String Manipulation
Author: Shahid Ali
"""

# -------------------------
# 1. What is a String?
# ---------------------------
# A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).

string1 = 'Hello'
string2 = "Python"
string3 = '''This is 
a multi-line string.'''

print(string1)
print(string2)
print(string3)


# ---------------------------
# 2. Accessing Characters in a String
# ---------------------------
word = "Python"
print("First character:", word[0])   # Indexing starts at 0
print("Last character:", word[-1])  # Negative indexing


# ---------------------------
# 3. String Slicing
# ---------------------------
print("Substring [0:4]:", word[0:4])   # Pyth
print("Substring [:3]:", word[:3])     # Pyt
print("Substring [2:]:", word[2:])     # thon

# ---------------------------
# 4. String Concatenation and Repetition
# ---------------------------
a = "Hello"
b = "World"
print(a + " " + b)   # Concatenation
print(a * 3)         # Repetition

# ---------------------------
# 5. String Functions / Methods
# ---------------------------
text = "   Python Programming   "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Stripped:", text.strip())
print("Length:", len(text))
print("Replace:", text.replace("Python", "Java"))
print("Find 'Pro':", text.find("Pro"))
print("Count 'm':", text.count("m"))





