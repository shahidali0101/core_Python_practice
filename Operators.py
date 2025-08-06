"""
Topic: Operators in Python
Author: Shahid Ali

"""

# ---------------------------
# What is an Operator?
# ---------------------------
# Operators are symbols that perform operations on variables and values.
'''
1. AIRRTHMETIC OPERATOR.
2. ASSIGNMENT OPERATOR.
3. COMPERISION OPERATOR.
4. LOGICAL OPERATOR.
5. IDENTITY OPERATOR.
6. MEMBERSHIP OPERATOR.

'''


# ---------------------------
# 1. Arithmetic Operators
# ---------------------------
a = 10
b = 3
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponent:", a ** b)        # 1000

# ---------------------------
# 2. Assignment Operators -[Are used to assign value to variable].
# ---------------------------
x = 5
x += 2   # x = x + 2
print("x after += 2:", x)

x *= 3   # x = x * 3
print("x after *= 3:", x)

# --------------------------------------------------------------
''' 3. Comparison Operators
----------------------------
                          -> compare values  between two variables.

                          =  Equal to 
                          != not equal to
                          >  Greater than 
                          <  Less than 
                          <= Less than equal to 
                          >= Greater than equal to'''

# -----------------------------------------------------------------
a = 10
b = 20
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ---------------------------
''' 4. Logical Operators
#----------------------------
            ●. AND-> It return true where all condition are True 
            ●. OR -> It return true when at least one condition are true.
            ●. NOT-> it reverse the condition of And or OR '''

                      
# ---------------------------
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# ---------------------------
''' 5. Identity Operators
#-----------------------------
            ● IS -> Returns True if both variables refer to the same object
            ● IS NOT-> Returns True if both variables do not refer to the same object'''
# ---------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)       # True
print("a is c:", a is c)       # False
print("a == c:", a == c)       # True (values are same)
print("a is c:", a is not c)   # True
# ---------------------------
''' 6. Membership Operators
#---------------------------Membership operators are used to check whether 
                            a value is present in a sequence like a
                            list, tuple, string, or set.

            ● IN  ->Check if value exist in list, tuple, string, or set.
            ● NOT IN ->Check if value not exist in list, tuple, string, or set'''
# ---------------------------
nums = [1, 2, 3, 4, 5]
print("3 in nums:", 3 in nums)
print("6 not in nums:", 6 not in nums)


