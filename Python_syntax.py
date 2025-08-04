# Topic: Basic Syntax and Print Statement
# Author: Shahid Ali.

#------------------------------------------------------------------------
# Python Syntax Basics
# ---------------------------
# Python uses indentation (whitespace) to define blocks of code.
# Each block of code (like loops, functions, conditionals)
#  must be consistently indented.

#-----------------------------------------------------------------------

# Valid indentation example: #✅
if True:
    print("This indent correct .")

# Invalid indentation would raise an error:  # ❌
if True:
print("it has  IndentationError")
#------------------------------------------------------------------------------
# ---------------------------
# The print() Function
# ---------------------------
# print() is used to display output on the screen

print("Hello, India!")
print("Python is bignner-friendly ")

# ---------------------------
# Printing Multiple Items
# ---------------------------
Name = "Shaid"
age = 25
print("My name is", Name, "and I am", age, "years old.")

# ---------------------------
# Escape Characters (\n)  .... to the new line.
# ---------------------------
print("This is a line break\nNext line starts here.")
print("they said, \"nothing is easy\"")

# ---------------------------
# Comments
# ---------------------------
# Single-line comment  [we use # to comment  single line]

#multi-line comment  
# To write a multiline comment in Python, we use triple quotes — either 
#      """  """   or '''  '''    
"""
This is a
multi-line comment  .
"""

'''This is a
multi-line comment,
 this is another line here '''