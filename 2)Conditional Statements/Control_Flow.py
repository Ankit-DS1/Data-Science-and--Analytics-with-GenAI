                            # CLASS - 6

# Control Flow Statements
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 1. if statement
# Syntax:

# if condition:
#     # code to be executed if condition is true
# Example:

age = 18
if age >= 18:
    print("You are eligible to vote.")

# 2. if-else statement
# Syntax:
# if condition:
#     # code to be executed if condition is true
# else:
#     # code to be executed if condition is false

# Example:
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 3. if-elif-else statement
# Syntax:
# if condition1:
#     # code to be executed if condition1 is true
# elif condition2:
#     # code to be executed if condition2 is true
# else:
#     # code to be executed if both condition1 and condition2 are false

# Example:

age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


#Example:

money = int(input("Enter the amount of money you have: "))

if money == 10:
    print("I will buy a chocolate.")
elif money == 20:
    print("I will buy a burger.")
elif money == 50:
    print("I will buy a pizza.")
else:
    print("I will save my money.")

#using logical operators 

a = 10
b = 20
c = 30

if a > b and a > c:
    print("A is the largest number.")
elif b > a and b > c:
    print("B is the largest number.")
else:
    print("C is the largest number.")