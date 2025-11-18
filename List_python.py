'''_____________________________ LIST __________________________________________________________
list is part of sequence data type which is a collection of repitative elements
it is used to store multiple data in single variable and its always written in square bracket
_________________________________________________________________________________________________

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


