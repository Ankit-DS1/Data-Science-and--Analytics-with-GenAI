#Inheritance:
#inheritance is the mechanism by which a class (child) can use the properties and methods of another class (parent).

#Types of Inheritance

#1.Single-Level Inheritance
#-> One class inherits from another.
#        Parent class ==> Child class

#2.Multiple Inheritance
#-> A class inherits from multiple parent classes.
#.        parent class 
#                        ==> child class
#         parent class

#3.Multilevel Inheritance
#->A class inherits from a class that is already a child of another class.
#       Parent class ==> Child class ==> Child class

#4.Hierarchical Inheritance
#-> Multiple classes inherit from a single parent class.
#.         Parent class ==> child class
#                             child class


#Example
class Animal:    #parent class, super class 
   def __init__(self,name,age):
       self.name = name
       self.age = age 
    
   def info(self):
       print(f"your name is {self.name} and your age is {self.age}")



class Human(Animal):  #child class, sub class
   def __init__(self, name, age , number, group):
       super().__init__(name, age)
       self.number = number
       self.group = group 


class Robots(Human):
   def __init__(self, name, age, number, group,imei):
       super().__init__(name, age, number, group)
       self.imei = imei

    
    



obj = Animal("lion",12)
obj2 = Human("Akarsh",24,1234567890,"B+")
obj2.info()

# Ex 2

class Animal:
   name = "Lion"

class Human:
   name = "Akarsh"

class Robots(Human,Animal):
   pass

class Animal:
   pass 

class Human(Animal):
   pass 

class Robots(Animal):
    pass 

