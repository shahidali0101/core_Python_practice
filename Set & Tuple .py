# ===========================
# TUPLES
# ===========================


'''TUPLE  -Tuple is a collection of repitative elements which is used to store the multipule
           Values in single Variable.
           Tuple is a part of sequence data type.

         1️⃣. Tuple written in round bracket ().
         2️⃣. Tuple are Ordered.
         3️⃣. Tuple are immutable or unchangable.
         4️⃣. Tuple also allow duplicate value.
         5️⃣. Tuple allow multiple type of data.
         6️⃣. Tuple are indexed.


                        --------------------------------           
                        #How to create a blank tuple 
                               x=()
                                      0r
                               y=tuple()
                        ----------------------------------
 ________________________________________________________________________________________________'''                       
''' add  100 in 3rd index of this tuple'''
# x=(45,78,89,45,56,23)
# x=list(x)
# x.insert(2,100)
# x=tuple(x)
# print(x)
#--------------

'''replace the first three value'''
# x=(45,78,89,45,56,23,90,)

# x=list(x)
# x[:3]=[200]
# print(x)
#--------------------
'''Delete two elements from tuple'''
# x=(45,78,89,45,56,23,90,)
# x=list(x)
# del x[-2:]
# print(x)
#----------------------------
'''Add 256 in last of this tuple'''
# x=(45,78,89,45,56,23,90,)
# x=list(x)
# x.append(256)
# print(tuple(x))
#-----------
''' Filter all even number store in new tuple'''
# x=(45,78,89,45,56,23,90,)
# x=list(x)
# y=[]
# for i in x:
    
#     if i%2==0:
#       y.append(i)
# print(tuple(y))
#------------------------------
'''________________________________________________________________________________________________________
PACKING    -> In this technique we divide the elements of tuple in Variable
              * there is total number of variable should be equal to total number of elements
              
UN-PACKING -> Number of Variable is less then number of values in tuple           
___________________________________________________________________________________________________________'''
# x=(10,20,30)
# a,*b=x
# print(b)  #[20,30]





'''___________________________________     SET      _______________________________________________________
   SET -> Set is a collection Non-repitative elements 
          which is used to store the multiple values
          in single variables
          
          
          1️⃣ Set written with curly Brackets {}.
          2️⃣ Set are Un-ordered.
          3️⃣ Set is changable.
          4️⃣ Set are not allow Duplicate Values.
          5️⃣ Set are Un-indexed.
          6️⃣Set allowed multiple type of Data                      
   ___________________________________________________________________________________________________________
                                            Differece between 
                     _________________________________________________________________
                             list        |       TUPLE         |        set 
                     -------------------------------------------------------------        
                1️⃣       []                      ()                       {}
                2️⃣    ORDERED    ✅     |   ORDERED   ✅      |   UN-ORDERED  ❌
                3️⃣    INDEXED    ✅     |   INDEXED   ✅      |   UN-INDEXED   ❌
                4️⃣    DUPLICATE  ✅     |   DUPLICATE ✅      |   NOT ALLOWED DUPLICATE ❌
                5️⃣     MUTABLE   ✅     |   IMMUTABLE ❌      |     MUTABLE   ✅ 

_________________________________________________________________________________________________________________                
# How to add element in set :  
          ADD     -> Its add elements in set we can not specify the order.

          UPDATE  -> It is used combine the two set.

          UNION   -> it is also used to combine the two set and add in new variable.
_________________________________________________________________________________________________________________
   
   '''

""" Add """
# x={34,56,67,89,3}
# x.add(200)
# print(x)
#--------------------------
""" UPDATE  """
# x={34,56,67,89,3}
# x.update({10})
# print(x)
#---------------------------
""" UNION  """
# x={1,2,3}
# y={4,5,6}
# z=x.union(y)
# print(z)
#--------------------------
'''creat a blank set'''
# x=set()
# print(type(x))   
#------------------------------
'''length of set elements'''
# x={23,45,23,23,23,23,23,89}
# print(len(x))      #3 bcoz set do not allow duplicates values