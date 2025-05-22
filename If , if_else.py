#Write a program to check if a number is positive.

num=int(input("enter no:"))
if num>0 :
    print("Positive")
else:
    print("Negative")


# Write a program to check whether a number is even or odd.

n=int(input("enter no  "))
if n%2==0 :
    print("Even")
else:
    print("odd")

#Write a program to check if the entered character is a vowel or consonant.

chr=input("Enter a charater ")
if chr in "aeiouAEIOU" :
    print("vowel")
else:
    print("Consonent")


#Write a program to check if a person is eligible to vote (age ≥ 18).

age=int(input("Enter Age "))
if age>=18 :
    print("Eligible")
else :
    print("Not Eligible")


#. Write a program to check if a number is divisible by 5 and 11.

num=int(input("enter number "))
if num%5==0 and num%11==0 :
    print(num ,"is divisible by both 5 and 11")
else :
    print(num ," is not divisible by both 5 and 11")
    
