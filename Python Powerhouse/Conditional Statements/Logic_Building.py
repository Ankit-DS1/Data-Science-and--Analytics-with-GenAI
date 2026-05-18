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

#4.Voting Eligibility 
#input name and age .if age is greater than or equal to 18,Print "Eligible to vote". If not,print how many years are left to become eligible.

name = input("Please enter your name:")
age = int(input("Please enter you age:"))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote.")
else:
    print(f"Hello {name}, you are not eligible to vote. You need to wait {18 - age} more years to become eligible.")


#5.Day Number to Day Name
#Take an integer(1-7) and print the corresponding weekday name(1 for Monday, 2 for Tuesday, etc.). Handle invalid inputs too.

day_name = int(input("Please Enter a number(1-7): "))

if day_name == 1:
    print("Monday")
elif day_name == 2:
    print("Tuesday")
elif day_name == 3:
    print("Wednesday")
elif day_name == 4:
    print("Thursday")
elif day_name == 5:
    print("Friday")
elif day_name == 6:
    print("Saturday")
elif day_name == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")


#6.Greatest of Three Numbers    
#Accept three numbers and find the greatesrt one among them using nested if-else.
#and also fid if 3 are equal also findif all are equal

a = int(input("Please Enter your first number: "))
b = int(input("Please Enter your second number: "))
c = int(input("Please Enter your third number: "))

if a == b and b == c:
    print("All three number are equal:")
elif a == b or b == c or c == a:
    print("Two number are equal:")
elif a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

#7.Leap year checker
#Input a year and check if it's a leap year using proper rules: divisible by 4, not by 100 unless divisible by 400.

year = int(input("Please Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("its a leap year")
elif year % 4 == 0:
    print("its a leap year")
else:
    print("its not a leap year")

#8. Shop Discount calclulator 
#Ask for purchase amount. Apply discount based on thresholdse.eg ,above 1000rs get 10% discount, above 5000rs get 20% discount. Print final bill.(you can also desingn a shop like interface later.)

bill = int(input("Please Enter your bill amount: "))

if bill > 1000 and bill <= 4999:
    print(f"you got a discount of 10% and your final bill is {(bill * 90)/100}")
elif bill > 5000:
    print(f"you got a discount of 20% and your final bill is {(bill * 80)/100}")
else:
    print("sorry you are not eligible for discount ")

#9.Vowel or Consonant Checker

char = input("Please Enter your Alphabet: ")

if char in 'aeiouAEIOU':
    print(f"{char} is a voweal")
else:
    print(f"{char} is a consonant")

