'''_______________________FILE HANDLING________________________________'''

'''file handling in python is a way of performing operations on files
    like opening,reading,writting and closing them.
    it allow us to store data permanently and 
    retrived it when needed
--------------------------------------------------------------------------------
OPEN() -: function is used to established a connection with a file .
          
          MODE-> READ | WRITE | APPEND | 
   
            R=Read the text file .
            W=write the text file .
            A=Append in text file or add in text file .
--------------------------------------------------------------------------------------
READ() -: IN python read function reads text from string .
-------------------------------------------------------------------------------
r=(read mode):- Opens a file for reading.
w=(write mode):-open a file for writting .
               if the file exist ,it content is truncate (emptied)
               if it dosen't exist ,a new file is created 

a=(Append Mode):- open a file for writing ,appending new content
                 to end of an existing file.
                 if the file Doesn't exist,a new is created.
 


'''
'''----------------------------------------------------------------------'''
# path=r"C:\Users\Shahid ali\Desktop\python_Notes.txt"
# data=open(path,"r")
# for i in data:
#     print(i)
'''------------------------------------------------------------------'''
'''print only four lines from the files'''

# import time 
# path=r"C:\Users\Shahid ali\Desktop\python_Notes.txt"
# data=open(path,"r")
# c=0
# for i in data:
#     if c==4:
#         break
#     else:
#          time.sleep(1)
#          print(i)
#     c+=1

"""with out loop"""  #Python is a high-level,----EXpected output
# path=r"C:\Users\Shahid ali\Desktop\python_Notes.txt"
# x=open(path,"r")
# y=x.read()
# y=y.split()
# z=" ".join(y[0:4])
# print(z)
# x.close()

'''store table in file ---------------WRITE MODE----'''
# path="C:/Users/Shahid ali/Desktop/python_Notes.txt"
# file=open(path,"w")
# x=10
# for i in range (1,11):   
#     file.write(f"{x}X{i}={x*i}\n")             
# file.close()
# print("Done")
#-----------------------------------------------------------
'''-----------------------APPEND MODE------------------------'''
# path="C:/Users/Shahid ali/Desktop/python_Notes.txt"
# file=open(path,"a")
# file.write("\n==========================================\n")
# x=10
# for i in range (1,11):    
#     file.write(f"{x}X{i}={x*i}\n")              
# file.close()
# print("Done")

#---------------------------------------------------------
'''----------File deleting-----------------'''

# import os
# path="C:/Users/Shahid ali/Desktop/python_Notes.txt"
# os.remove(path)
# print("Done! \n deleted")

