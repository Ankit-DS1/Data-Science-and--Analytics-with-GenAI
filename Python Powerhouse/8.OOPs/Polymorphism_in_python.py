# Polymorphism

# -> Polymorphism allows different classes to define methods with the same name but different behaviors
# -> In Python, it is typically achieved through method overriding.

# Types of polymorphism

# Method Overloading:
# -> Python simulates method overloading using default or variable-length arguments,as it doesn't support traditional overloading.

# Method Overriding:
# -> Occurs when a subclass defines a method with the same name as its superclass, replacing the superclass's method.

# Ex -1 

class Animal:
    name = "lion"
    def speak(self):
        print("Hellow i roar")

class Bird:
    name = "Sparrow"

    def speak(self):
        print("Hello i tweet")

obj = Animal()
obj2 = Bird()

obj.speak()
obj2.speak()

#Ex -2 


class Animal:
    name = "lion"
    def speak(self):
        print("Hellow i roar")

class Human(Animal):
    name = "Ankit"

    def speak(self):
        super().speak()
        print("Hello my name is Ankit")

obj = Human()
obj.speak()
