                          #Data structures in Python

#Data structures are a type of storage in which we can store multiple values 
#In-built data structures in Python are:
#1. List
#2. Tuple
#3. Set
#4. Dictionary

#Customized data structures in Python are:
#1. Stack
#2. Queue
#3. Linked List
#4. Tree
#5. Graph

                          #List in Python

#List is a collection of items which are ordered and changeable.
#List are written with square brackets [].
#List is hetrogeneous Nature, it can contain different types of data.
#list can also store duplicate values.
#list is mutable, we can change the values in the list.

#Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

#List indexing and slicing 

l = [13,23,45,67,89]
print(l[:3]) #slicing the list from index 0 to 2
print(l[2:]) #slicing the list from index 2 to the end
print(l[:-3]) #slicing the list from the beginning to index -4


#Exmple of mutability of list
a = [1, 2, 3, 4, 5]
a[2] = 10
print(a)

#reference copy
a = [10, 20, 30, 40, 50]
b = a
b[2] = 100
print(a) #both a and b will be changed because they are referencing the same list
print(b) 

#Shallow copy
a = [10, 20, 30, 40, 50]

b = a.copy() #shallow copy of list a
b[2] = 100
print(a) 
print(b) 

#Deep copy
import copy
a = [10, 20, 30, 40, 50]
b = copy.deepcopy(a) #deep copy of list a
b[2] = 100
print(a) 
print(b) 

#Traversing a list

 #Method 1

a = [10,20,30,40,50]

for i in a:
    print(i)

#Method 2 (index)

a = [10,20,30,40,50]

for i in range(len(a)):
    print(a[i])

#List Methods

help(list) #to see all the methods available for list

#Append() method is used to add an item to the end of the list.
a = [10,20,30,40,50]
a.append(60)
print(a)

#clear() method is used to remove all the items from the list.
a = [10,20,30,40,50]
a.clear()
print(a)

#count() method is used to count the number of times an item appears in the list.
a = [10,20,30,40,50,10,20]
print(a.count(10)) #counting the number of times 10 appears in the list

#index() method is used to find the index of the first occurrence of an item in the list.
a = [10,20,30,40,50,10,20]
print(a.index(10))

#insert() 
a = [10,20,30,40,50]
a.insert(3,93)
print(a)

#pop() 
a = [10,20,30,40,50]

pooped = a.pop(0)
print(a)
print(pooped)

#sort()

a = [10,20,30,40,50,23,45,67,86,43,22,34]
a.sort()
print(a)












