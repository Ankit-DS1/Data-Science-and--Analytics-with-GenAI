'''
Instance attribute:
-> A attribute created using the self keyword or
say an attribute created using self keyword
like self.name , self.age etc

Class attribute:
-> Attribute created inside a class without using
the self keyword.

Instance Method :
-> A Method created using the self key word as
parameter.

Class method:
-> Class methods use the @classmethod
decorator and do not rely on instance-
specific data.

Satic method:
-> A static method is a method inside a class that
does not depend on any specific instance of
the class (unlike instance methods, which use
self). It is defined using the @staticmathod
decorator and does not take the self or cls
parameter as its first argument.

'''

# Ex-1

class Animal:
    gender = "Male" # class attribute

    def __init__(self,name,age):
       self.name = name #instance attribute
       self.age = age  #instance attribute

    def info(self):  #instance method
         print("this is a method")
    
    @classmethod
    def clmethod(cls): #class method
        print(f"{cls.gender} is your gender")
    
    @staticmethod
    def hello():  #static method
       print("hello I am a static method")



obj = Animal("Lion",12)

obj.info()

obj.clmethod()

obj.hello()


#make a student regestration system ask for name, age, number, blood group register 3 students 
class Regestration:
    def __init__(self,name,age,number,blood):
        self.age = age
        self.name = name 
        self.number = number 
        self.blood = blood 
    
    def info(self):
        print(f"hello your name is {self.name}\nyour age is {self.age}\n your number is {self.number}\nyour blood group is {self.blood}")

student1 = Regestration("Satyam",24,9907666412,"B+")
student2 = Regestration("Rishab",22,9907666411,"A+")
student3 = Regestration("Ankit",23,9907666414,"O+")

student2.info()
student3.info()
