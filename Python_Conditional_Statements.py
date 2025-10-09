# Python_Conditional_Statements.py
"""
Topic: Conditional Statements in Python
Author: Shahid Ali  

"""

# -------------------------------- 
# What are Conditional Statements?
# --------------------------------
# Conditional statements are used to perform different actions based on different conditions.
# Python uses if, elif, and else keywords for decision making.

# ---------------------------
# Basic if Statement
# ---------------------------
age = 20
if age >= 18:
    print("You are eligible to vote.")

# ---------------------------
# if-else Statement
# ---------------------------
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ---------------------------
# if-elif-else Ladder
# ---------------------------
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or below")

# ---------------------------
# Nested if Statements
# ---------------------------
x = 10
y = 20
if x > 5:
    if y > 15:
        print("Both conditions are True")

# ---------------------------
# Using Logical Operators with Conditions
# ---------------------------
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")



#--------------------------------------------------------------
''' Write a Python program to calculate tax based on income:
            take input by user
              Income > 15,00,000 → 30% tax
              Income > 12,00,000 → 20% tax
              Income > 10,00,000 → 10% tax
              Income > 7,00,000 → 5% tax
              Otherwise → No tax'''
income=float(input("enter income: "))
if income>1500000:
        print(income*0.30) 
elif income>1200000:
        print(income*0.20)
elif income>1000000:
          print(income*0.10)
elif income>700000:
          print(income*0.05)          
else:
     print("no tax")   

#--------------------------------------
'''Write a program to categorize temperature: 
                                          <0 = Freezing 
                                          0-10 = Cold 
                                         11-25 = Moderate 
                                           25 = Hot '''
x=float(input("enter temp: "))
if x<0:
    print("freezing")
elif x<10:
    print("cold")
elif x<25 :
    print("moderate")   
else:
    print("hot")

#------------------------------------------
""" Write a program to assign grades based on marks: 
                                        o 90+ = A 
                                        o 80-89 = B 
                                        o 70-79 = C 
                                        o Below 70 = F """
x=float(input("enter marks: "))
if x>90:
    print("A",x)
elif x>80:
    print("B",x)
elif x>70:
    print("C",x)
else:
    print("F",x )

#--------------------------------------------------

'''Take an integer input.
       Print "low" if it's between 1 and 20
       Print "mid" if it's between 21 and 30
       Else, print "high"'''

x=int(input("enter no: "))
if x>=1 and x<=20:
    print("low")
elif x>=21 and x<=30:
    print("mid")
else:
    print("high")    


''' Write a program to find the greatest among three numbers.'''

x=float(input("enter no: "))
y=float(input("enter no: "))
z=float(input("enter no: "))
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)  

#---------------------------------------
"""Print Numbers 0 to 20 Except (5, 10, 15 )"""

for i in range(0,21):
    if i==5 or i==10 or i==15: 
      continue
    print(i)

''' Print numbers from 1 to 20.
         Skip numbers between 8 and 12'''

for i in range(1,21):
    if i>=8 and i<=12:
       continue
    print(i)

for i in range(1, 21):
    if 8 <= i <= 12:
        continue
    print(i)

''' WAP take input from user and print last digit of that number.'''

x=int(input(" enter any number-:  "))
y=x%10
print("this is the last digit:-",y)










