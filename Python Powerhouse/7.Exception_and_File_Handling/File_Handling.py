                                # File Handling

#File handling in python , as the name suggest it deals with files with python
#It means creating,reading,updating and deleting (CRUD) operation in different files.


# File handling Functionalities 

 #open() - to open a file we need to write open() it accepts two parameters, 1st location of the file, 2nd mode of thr file("r","a","w","x")

 # "r" - For reading the file.error if file does not exist.
 # "a" - For appending in file. creates a file as well.
 # "w" - overwriting the file.creates if it does not exist.
 # "x" - create a file.error if file already exist.

#Example

file = open("function.py")

print(file.read())

#Example


file = open("push.txt",'w')

file.write("Hello i am ankit ,hi")

file.close()

#Example

with open("function,py",'r') as fs:
    print(fs.read())
    
