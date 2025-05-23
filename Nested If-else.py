# Write a program to find the greatest among three numbers.

num_1=int(input("Enter first number :"))
num_2=int(input("Enter second number:"))
num_3=int(input("Enter third number :"))
if num_1>num_2 and num_1>num_3:
    print(num_1," num_1 is Greater")
else:
    if num_2>num_1 and num_2>num_3 :
        print(num_2 ," num_2 is Greater")
    else:
         print(num_3, "num_3 is Greater ")

#Write a program to check whether a number is positive, negative, or zero using nested 
#if.

num=int(input("enter no:"))
if num>0 :
    print(num,"Positive")
else :
    if num==0 :
        print(num ,"zero")
    else:
        print(num,"Negative")


'''Write a program to assign grades based on marks: 
o 90+ = A 
o 80-89 = B 
o 70-79 = C 
o Below 70 = F
'''


marks=int(input("enter Marks :"))
if marks>=90 :
    print("A")
else:
    if marks>=80 :
        print("B")
    else:
        if marks>=70 :
            print("C")
        else:
            print("F")



#Write a program to classify a triangle based on side lengths (equilateral, isosceles, or 
#scalene)

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Equilateral")     #All sides are equal
    else:
        if a == b or a == c or b == c:
            print("Isosceles")    #two sides are equal
        else:
            print("Scalene")      #all sides are different



#Write a program to check whether a year is a leap year using nested if.

year=int(input("Enter year"))
if year%4==0 and year%100==0:
    print(year ,"is a Leap year")
else:
    if year%4==0 and year%100!=0:
        print(year, " Is a leap year")
    else :
        print("Is not a leap Year")




        















