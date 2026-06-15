# While Loop Logic Building

#1.Print Each Digit(Reverse Order)
 #Break a number into individual digits and print them starting from the last digit.

a = int(input("Enter a number: "))

while a > 0:
    print(a % 10)
    a = a // 10

#2. Sum of Digits
#Add all the digits of a number.

a = int(input("Enter a number: "))
s = 0

while a > 0:
    s = s + a % 10
    a = a // 10

print(f"sum of digits: {s}")

#3. Reverse a Number
 #input a number and reverse its digits.

a = int(input("Enter a number: "))
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(f"reversed number: {rev}")

#4.Palindrome Number check
 #check if a number reads the same forward and backward.

a = int(input("Enter a number: "))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if copy == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#5.Automorphic Number 
#A number is automrphism if its square end with the number itself(e.g. 5^2 = 25, 6^2 = 36).

a = 25
dup = a 
square = a ** 2

count = 0
while a > 0:
    count = count + 1
    a = a // 10

    extract = square % (10 ** count)

    if extract == dup:
        print("Automorphic")
    else:
        print("Not Automorphic")

        