
"""
Topic: Variables and Data Types
Author: Shahid Ali.

"""

# ------------------------------------------------------------------------
# What is a Variable?
# ------------------
# A variable is a container for storing data values.
#---------------------------------------------------

#Limitation of vaariable -
#            ● Variable should start with alphabet.    v1= ✅ |  1v= ❌
#            ● Variable is case senstive.
#            ● Variable can't conatain any special charactor.
#            ● Variable can alphanumeric.
#            ● Variable can contain _ underscore.
#---------------------------------------------------------------------------

# Syntax: variable_name = value
name = "Shahid"      # string
age = 25            # integer
height = 5.8        # float
is_student = True   # boolean

# ---------------------------
# Displaying Variable Types
# ---------------------------
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# ---------------------------
# Multiple Variable Assignment
# ---------------------------
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Assigning the same value to multiple variables:
a = b = c = 100
print(a, b, c)

# ---------------------------
# Data Types in Python
# ---------------------------
# 1. Text Type      : str
# 2. Numeric Types  : int, float, complex
# 3. Sequence Types : list, tuple, range
# 4. Mapping Type   : dict
# 5. Set Types      : set
# 6. Boolean Type   : bool
# 7. Binary Types   : bytes, bytearray, memoryview
# 8. None Type      : none
# ---------------------------
# Type Casting
# ---------------------------
s_num = "10"
i_num = int(s_num)  # convert string to integer

print(i_num + 5)    # Output: 15





