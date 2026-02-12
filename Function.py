# Python_Functions.py


'''
# ---------------------------
# What is a Function?
# ---------------------------
# A function is a block of reusable code that performs a specific task.
# Functions help in code reusability and make programs easier to manage.

# Syntax:
# def function_name(parameters):
#     """docstring (optional)"""
#     # block of code
#     return value (optional)                                  '''


# ---------------------------
# 1. Defining and Calling a Function
# ---------------------------
def greet():
    """This function prints a greeting message"""
    print("Hello, welcome to Python functions!")

# Calling the function
greet()


# ---------------------------
# 2. Function with Parameters
# ---------------------------
def greet_user(name):
    """Greets the user with their name"""
    print(f"Hello, {name}! Have a great day.")

greet_user("Alice")
greet_user("Bob")


# ---------------------------
# 3. Function with Return Value
# ---------------------------
def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)


# ---------------------------
# 4. Default Parameters
# ---------------------------
def power(base, exponent=2):
    """Calculates power with default exponent = 2"""
    return base ** exponent

print("5 squared:", power(5))
print("2^3:", power(2, 3))


# ---------------------------
# 5. Keyword Arguments
# ---------------------------
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Charlie")


# ---------------------------
# 6. Arbitrary Arguments (*args)
# ---------------------------
def sum_all(*numbers):
    """Takes any number of arguments and returns their sum"""
    return sum(numbers)

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))


# ---------------------------
# 7. Arbitrary Keyword Arguments (**kwargs)
# ---------------------------
def user_info(**info):
    """Accepts keyword arguments and prints them"""
    for key, value in info.items():
        print(f"{key}: {value}")

user_info(name="David", age=30, city="New York")


# ---------------------------
# 8. Lambda Functions (Anonymous Functions)
# ---------------------------
# Lambda functions are small, one-line functions without a name.
square = lambda x: x * x
print("Square of 6:", square(6))


# ---------------------------
# 9. Recursion in Functions
# ---------------------------
# A function that calls itself.
def factorial(n):
    """Returns factorial of a number using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
