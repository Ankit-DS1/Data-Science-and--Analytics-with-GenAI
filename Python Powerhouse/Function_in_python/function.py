#Function in Python
  #Function is a block of code which only runs when it is called. We can pass data, known as parameters, into a function. 
  #A function can return data as a result.

#Creating a Function

def Greet(): #defining a function
    print("Hello, World!")

Greet() #this is calling the function

#return statement is used to exit a function and return a value.

def Greet():
    return "Hello, World!"

print(Greet())
       #or
result = Greet() #this is calling the function and storing the return value in a variable
print(result)

# Parameters and Arguments

def addition():
    a = 5
    b = 10
    print(a + b)
addition() #this is calling the function


def addition(a, b): #a and b are parameters
    print(a + b)

addition(5, 10) #5 and 10 are arguments
addition(20, 30) #20 and 30 are arguments


# Pallindrome or Not 

def pallindrome(x):
    rev = 0
    copy = 0

    while x > 0:
        rev = (rev * 10) + (x % 10)
        x = x // 10
    
    if copy == rev:
       return True
    else:
       return False
    
print(pallindrome(121)) #True
print(pallindrome(-121)) #False
print(pallindrome(10)) #False

#Keyword Arguments

def addition(a, b):
    print(a + b)

addition(b= 5, a = 10) #this is calling the function with keyword arguments


def addition(a, b, c):
    print(a + b + c)

addition(5, c = 10, b = 15) 