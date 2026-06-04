                         # Set

# A set is an unordered collection of unique elements. 
#it is defined by curly braces {} or the set() constructor.
#you can only store hashable (immutable) value inside a set.
#No indexing or slicing allowed.
#No duplicate elements allowed.
#Unordered collection, so the elements do not maintain any specific order.

#1. Creating a set
my_set = {1, 2, 3, 4, 5,(1,2,3,4,5),True,"Hello"}
print(my_set)

#Set constructor

a = [1,2,3,4,4,4,4,5,5,6,6,7,8,9,10,10,10]
s = set(a)
print(s)

#Traversing on the set

s = {1, 2, 3, 4, 5,(1,2,3,4,5),True,"Hello"}

for i in s:
    print(i)

#set Methods

s = {1, 2, 3, 4, 5,6,8,9}

s.add(10)
s.clear()

print(s)

#Difference

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.difference(s2)) 
print( s2 - s1)

#Discard 
s1 = {1, 2, 3, 4, 5}
s1.discard(3)
print(s1)

#Intersection
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.intersection(s2))
print(s1 & s2)

#symmetric_difference
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

#union
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))
print(s1 | s2)

