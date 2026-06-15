#Dunder/Magic Methods
#-> Dunder methods are special methods in Python that define object behavior for built-in operations. 
#-> They are prefixed with double underscores (e.g., __init__, __str__).

# Common Dunder/Magic Methods

#__init__(self, ...):
# -> Constructor, called when an object is created.

#__add__(self, other):
# -> Defines behavior for the + operator.

#__eq__(self, other):
#-> Defines behavior for the == operator.

# __getitem__(self,key):
# -> Allows indexing like lists dictionaries.

#__str__(self):
# -> string representation of an object.

#__len__(self):
# -> Returns the length of an object, used by len().


#Example -1


class Students:
    def __init__(self,name ,marks):
       self.name = name
       self.marks = marks 
    
    def __str__(self):
       return f"{self.name} is your name and your marks are {self.marks}"

obj = Students("Akarsh",95)

print(obj)

#Example 2

class Shopping:
   def __init__(self,items):
       self.items = items
    
   def __len__(self):
        return len(self.items)

obj = Shopping(['apple',"milk","bread"])
obj2  = Shopping(["apple","banana"])

print(len(obj2))

#Example 3

class Numbers:
    def __init__(self,number):
         self.number = number 
        
    def __add__(self,custom):
       return self.number + custom.number

obj1 = Numbers(12)
obj2 = Numbers(34)

print(obj1 + obj2)

