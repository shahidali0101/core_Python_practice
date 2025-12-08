'''_____________________________ LIST __________________________________________________________
list is part of sequence data type which is a collection of repitative elements
it is used to store multiple data in single variable and its always written in square bracket
_______________________________________________________________________________________________
 
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
   -------------------------------------------------------------------------------------------
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
'''_________________________________ ADD ELEMENTS IN LIST_____________________________________________
1.INSERT  : With the help of this function we can add element in LIST by index number.
2.APPEND  : Append are used to add value in last of index value.
3.EXTEND  : Its combine two or more than two list in last of position.
______________________________________________________________________________________________________ '''
x=["a","b","c","d"]
x.insert(2,"Python")
print(x)                   #['a', 'b', 'Python', 'c', 'd']
#-----------------------
x=["a","b","c","d"]
x.append("Prince")
print(x)                 #['a', 'b', 'c', 'd', 'Prince']
#-----------------------
x=["a","b","c","d"]
x.extend([10,20,30])
print(x)                 #['a', 'b', 'c', 'd', 10, 20, 30]
#-----------------------
x=["a","b","c","d"]
y=[1,2,3,4,5]
x.extend(y)
print(x)                #['a', 'b', 'c', 'd', 1, 2, 3, 4, 5]
#_______________________________________________________________________________  

'''WAP to store all even number in list from 1 to 20'''
x=[]
for i in range(1,21):
    if i%2==0:
       x.append(i) 
print(x)


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.POP   :-it delete elements from list by index number and 
          by default delete the last elements from list.

2.REMOVE:-its delete elements from list by value " " .

3.CLEAR :-its delete entire elements from list   .

4.DEL   :-Its a keyword in python which is used to delete the value and variable also.
_______________________________________________________________________________________________ '''
x=["one","two","three","four","five"]
x.pop() #delete last element
x.pop(1) #delete element by index
#----------------------------------------------------------------------------------------------
x=["one","two","three","four","five"]
x.remove("two") #only single value in one tym
#--------------------------------------------------------------------------------------
x=["one","two","three","four","five"]
x.clear()
#--------------------------------------------------------------------------------------

x=["one","two","three","four","five"]
del x       #delete completely even variable.
del x[0:2]  #deleting elements by indexing  .
_____________________________________________________________________________________________________

x=["one","two","three","four","five"]
y=["six","seven","eight"]
print(x+y)

#_________________________________________________________________________________________________
'''delete all 23 from list '''
x=[34,23,23,12,34,23,15]
while 23 in x:
        x.remove(23)
print(x) 
#-----------------------------------------------
'''WAP to store all name in new list which name start with "a" '''
x=["Aman","Ravi","Alok","Jimmy","Roy","Aryan"]
y=[]
for i in x:
    if i[0].lower()=="a":
        y.append(i)
print(y)
#-----------------------------------------------------------------------------


'''print all common elements from x and y '''
x=[12,23,45,56,78]
y=[47,58,12,45,10]
z=[]
for i  in x:
    if i in y:
        z.append(i)
print(z)
'''create a blank list and store all text data'''
y=[]
x=["SQL",45,25j,True,14,"excel","python"]
for i in x:
    if type(i)==str:
       y.append(i)
         
print(y)
#-----------------------------------------------
'''Creat a blank list and add unique values'''
y=[]
x=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]
for i in x:
    if i not in y:
        y.append(i)
print(y)

'''______________________________________________________________________________________
SORT--its arrange the data in ascending or descending order in orginal list
SORTED---its also arrange data in ascending or descending order but it store in new variable.
_________________________________________________________________________________________________'''

















