                            #Tuples 

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Tuple has hetrogeneous data types and allows duplicate values.

#Tuple has a immutable data type, which means that once a tuple is created, you cannot change its values.

#creating a tuple
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)

#Tuple unpacking is also possible, which allows you to assign the values of a tuple to individual variables in a single line of code.
a,b,c =(1,3,5)
print(b)

#index and slicing in tuple

a = (1, 2, 3, 4, 5)
print(a[:3]) #slicing

a = [1,2,3,4,5]
my_tuple = tuple(a)
print(my_tuple)

#Traversing a tuple

#1st
t = (1, 2, 3, 4, 5)
for i in t:
    print(i)

#2nd

t = (1, 2, 3, 4, 5)
for i in range(len(t)):
    print(t[i])

#tuple methods

help(tuple)

a = (1, 2, 3, 4, 5,5,6,4,3,2)
print(a.count(5)) #count the number of times a value appears in a tuple
print(a.index(4)) #returns the index of the first occurrence of a value in a tuple