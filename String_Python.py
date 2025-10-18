# Python_Strings_Manipulation.py
"""
Topic: Strings in Python & String Manipulation
Author: Shahid Ali
"""

# ------------------------
# 1. What is a String?
# ------------------------
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


# ---------------------------
# 6. Checking String Types
# ---------------------------
num = "12345"
alpha = "Hello"
alnum = "Hello123"

print("Is digit?", num.isdigit())
print("Is alpha?", alpha.isalpha())
print("Is alphanumeric?", alnum.isalnum())

# ---------------------------
# 7. String Formatting
# ---------------------------
name = "Alice"
age = 25

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# Using format()
print("My name is {} and I am {} years old.".format(name, age))

# ---------------------------
# 8. Splitting and Joining Strings
# ---------------------------
sentence = "Python is fun to learn"
words = sentence.split()  # Converts string to list
print("Split:", words)

joined = "-".join(words)  # Joins list back into string
print("Joined:", joined)

# ---------------------------
# 9. String Iteration
# ---------------------------
for char in "Hello":
    print(char)

# ---------------------------
# 10. String Reversal
# ---------------------------
s = "Python"
print("Reversed:", s[::-1])

# ---------------------------
# 11. Palindrome Check (Practice)
# ---------------------------
def is_palindrome(word):
    return word == word[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'python' a palindrome?", is_palindrome("python"))


#_________________________________________________________________________________________
#                          Questions
#------------------------------------------------------------------------------------------

'''  show the lenth of the text without space '''

x="python is a programming language"
y=len(x)-x.count(" ")
print(y)
#-------------------------OR

y=x.replace(" ","")
print(len(y))

#----------------------------------------------------------------------------------------------------

'''  Write a Python program to convert a string to uppercase if its length > 5 else to lowercase '''
x=input(enter ")
if len(x)>=5:
    print(x.upper())
else:
    print(x.lower())
#--------------------------------------------------------------
''' WAP by user input ,if name startwith "p","r","a" or "m" 
     then show "yes" else show "No"   '''
x=input("enter word:")
if x[0] in ("pram"):
    print("yes")
else:
    print("no")

''' WAP to check id name start and endswith "a" then show "yes" else "NO". '''
x=input("enter name:")
if x[0]=="a" and x[-1]=="a":
    print("yes")
else:
    print("no")  
#                          ---OR---
x=input("enter name:")
if x.startswith("a") and x.endswith("a"):
    print("yes")
else:
    print("no") 

#-----------------------------------------
'''   replece i with this "*" '''
x="India is a Incredible country".lower()
y=x.replace("i","*")
print(y)
#----------------------------------------------------
''' replece i with this "*" and rest of it print in capital'''

x=input("enter word:").lower()
y=x.replace("i","*")
print(y.upper())

#--------------------------------------------










