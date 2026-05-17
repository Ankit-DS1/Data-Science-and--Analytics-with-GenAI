#1.Compare two numbers
   #Take two numbers as input and determine number is greater --or if they're equal.

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

if a > b:
    print(F"{a} is greater than {b}")
elif a < b:
    print(F"{b} is greater than {a}")
else:
    print(F"{a} and {b} are equal")

#2.Greet by Gender(m/f)
#Accept a gender input('m' or 'f')and printa greeting like "Hello Sir" for 'm' and "Hello Ma'am

gen = input("Please tell your gender (m/f) : ")
if gen == 'm' or gen == 'M':
    print("Hello Sir")
elif gen == 'f' or gen == 'F':
    print("Hello Ma'am")
else:
    print("Invalid input")

#3.Even or odd checker 
#Accept a number from the user and check whether it's even or odd using modulo(%).

a = int(input("Please enter a number : "))

if a % 2 == 0:
    print(F"{a} is an even number")
else:
    print(F"{a} is an odd number")

#4.V