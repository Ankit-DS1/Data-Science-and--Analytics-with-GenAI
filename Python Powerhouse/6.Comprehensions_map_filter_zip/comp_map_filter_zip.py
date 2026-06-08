                             #some Advance stuff

#lambda expression

square = lambda a : print(a**2)
square(12)

add = lambda x,y : x+y
print(add(12,34))


#Map

#Purpose Apply function to every item of an iterable and return a new iterable

#syntax = map(function, iterable)

def square(x):
    return x**2

a = [1,2,3,4]
l = map(lambda x :x **2, a)
print(list(l))

#Filter
#Purpose - Filter items from an iterable based in a condition 

#syntax - filter(function, iterablr)

a = [1,2,3,4,5,6]

l = filter(lambda x : x%2 == 0,a)
print(list(l))

#Zip 
#Purpose - combine multiple iterable into pairs of elements.

#syntax = zip(iterable1, iterable2, ......)

name = ["Ankit", "Rishab","Rani"]
ages = [22,23,21]

comb = zip(name,ages)
print(dict(list(comb)))

#List comprehensions

a =[1,2,3,4,5,6,7,8]

l = [i for i in a if i % 2 == 0]
print(l)

# Dict comprehensions

a =[1,2,3,4,5,6,7,8]

l = {i:i**2 for i in a if i%2 == 0}

print(l)

#Generators

#Purposr: Generators are a special type of iterator that generate items one by one instead of storing thr entire sequence in memory.
#use - saves memory for large datasets
#Efficient for lazy evalution(compute values only when needed)


def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(list(gen))

#comprehensions

sequence = (x**2 for x in range(5))

print(next(sequence))
print(next(sequence))

#Decorators

def my_decorator(func):
    def wrapper():
        print("Hello i will print before")
        func()
        print("Hello i will print after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

def decorate(func):
    def wrapper(a,b):
        print("Your 2 numbers addition is: ")
        func(a,b)
        print("Thank your for using us")
    return wrapper


@decorate
def addition(a,b):
    print(a+b)

addition(12,12)






 