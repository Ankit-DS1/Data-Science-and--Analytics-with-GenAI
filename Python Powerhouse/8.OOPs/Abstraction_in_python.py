# Abstraction
#-> Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
#-> It is used to define a common interface for different sub classes.

# Abstract Classes and Methods

#Abstract Class:
#-> A class that contains one or more abstract methods.

#Abstract Method:
#-> A method that is defined but not implemented in the abstract class.
#-> Subclasses must provide the implementation.


# In Python, we use the to define abstract classes and methods.

# Ex-1

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 
   


class Dog(Animal):
    def sound(self):
        print("Hello I make woff sound!")
    def hello(self):
        print("I am a dog and I woof")

class cat(Animal):
    def sound(self):
        print("hello I make meow sound")

obj = Dog()