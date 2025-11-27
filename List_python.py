'''_____________________________ LIST __________________________________________________________
list is part of sequence data type which is a collection of repitative elements
it is used to store multiple data in single variable and its always written in square bracket
________________________________________________________________________________________________

1-list are written in square bracket.
2-list are mutable or changable.
3-list are used to store multiple values in a single variable.
4-list are ordered.
5-list allowed duplicate value.
6-list are indexed.
7-list support Multiple type of data  
                          
                        ----------------------------------------
                        #how to create a blank list  
                          x=[]
                          print(type(x))     #class list
                          print(len(x))      # 0
                          
                          x=list()
                          print(x)
                        ----------------------------------------
   ------------------------------------------------------------------------------------------
   0-list consider " , "comma in last✅ but in begining or mid it will show error❌                      
---------------------------------------------------------------------------------------------------
INDEXING - Iindexing are used to Extract the single elements from list.
SLICING  - Slicing are used to extract the range of elements from list.
---------------------------------------------------------------------------------------------------

______________________________________________________________________________________________________'''



# ---------------------------
# 1. What is a List?
# ---------------------------
# A list is a mutable (changeable), ordered collection of items.
# Lists can store different data types.


fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 10, 5.5, True]


print(fruits)
print(numbers)
print(mixed)


# ---------------------------
# 2. Accessing List Elements
# ---------------------------
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# ---------------------------
# 3. Modifying a List (Mutable)
# ---------------------------
fruits[1] = "mango"
print("Updated fruits:", fruits)


# Add items
fruits.append("orange")
fruits.insert(1, "kiwi")
print("After adding items:", fruits)


# Remove items
fruits.remove("apple")
popped_item = fruits.pop() # removes last item
print("After removing items:", fruits)
print("Popped item:", popped_item)


# ---------------------------
# 4. List Slicing
# ---------------------------
print("Sliced list:", numbers[1:3])
print("First three:", numbers[:3])
print("From index 2:", numbers[2:])


# ---------------------------
# 5. List Functions / Methods
# ---------------------------
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Squares:", squares)


#------------------------------------------------------------------------------
#EXTRACT ELEMENTS
x=[10,20,30,40,50,60,70,80,90]
# [70,60]
print(x[-3:-5:-1]) # OR   x[6:4:-1]

# [10,30,50]
print(x[0:5:2])     #OR   x[-9:-4:2]

# [40,50,60]
print(x[3:6])       

# [90,80]
print(x[-1:-3:-1])

# [90,60,30]
print(x[-1::-3])
#----------------------------
x = [[14,78,59,26,23,[8,7,5,4]]]
#[78,59]
print(x[0][1:3])

#[7,5]
print(x[0][5][1:3])

#[4,5,7,8]
print(x[0][5][-1::-1])

#[14,23]
print(x[0][0:6:4]) 
#----------------------------------------------------------------
'''Count total "A" ,"a"  '''
x=["a","b","c","A","a","C"]
c=0
for i in x:
    if i.lower()=="a":
        c+=1
print(c)    
#------------------------OR
c=0
for i in x:
    if i=="a" or i=="A":
        c+=1
print(c)
#-----------------------OR
c=0
for i in x:
    if i in "Aa":
        c+=1
print(c)
#-------------------------OR
print(x.count("a")+x.count("A"))


#-------------------------------------------------------------------
