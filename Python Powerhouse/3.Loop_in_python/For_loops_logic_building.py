
#1.Print "Hello world" n times
#use a loop to repeat the print statement("Hello world") based on user input count n.

n = int(input("How many times do you want to print: "))

for i in range(n):
    print(f"{i+1}. Hello world")

#2.Print number from  1 to n
#Display number in increasing order from 1 up to a give number n.

n = int(input("Please enter a number: "))
for i in range(1,n+1):
    print(i)

#3.Print number from n to 1
#Display number in decreasing order from  n down to 1

n = int(input("Please Enter a number:"))   

for i in range(n,0,-1):
    print(i)

#4.sum of Natural numbers
#Take input n and calculate the total sum from 1 to n.

n = int(input("Please enter a number: "))

s = 0
for i in range(1,n+1):
    s = s + i
print(f"The sum of first {n} natural numbers is: {s}")


#5.Factorial of a number
#calculate the factorial (n!) using a loop -- multiplying numbers from 1 to n.

n = int(input("Please enter a number: "))

fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"The factorial of {n} is: {fact}")

#6.Sum of Even and odd number in range 
#from 1 to n, find and print the sum of all even and all odd numbers separately.

n = int(input("Please enter a number: "))
even_sum = 0
odd_sum = 0

for i in range (1,n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of even numbers from 1 to {n} is: {even_sum}")
print(f"The sum of odd numbers from 1 to {n} is: {odd_sum}")

#7.Print all factors of a number 
#Display all number that divide the input number exactly (no remainder).

n = int(input("Please enter a number: "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)

#8.Sum of all factors
#add up all the factors found in the previous question (excluding or including the number itself  -your choice).

n = int(input("What number do you want to find the sum of factors for? :"))

s = 0

for i in range(1,n+1):
    if n % i == 0:
        s = s + i
print(f"The sum of factors of {n} is: {s}")

#9.Power calculation (a^b)
#input base a and exponent b, and calculate the result using a loop (without using **)

a = int(input("Please enter the base number: "))
b = int(input("Please enter the exponent: "))

power = a 
for i in range(1,b-1):
    power = power * a 

print(f"{a} raised to the power of {b} is: {power}")

#9.prime Number check 
#Accept a number and check if it divisble only by 1 and itself(i.e,Prime or not).

n = int(input("Give your number(to check if it's prime): "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1

if count == 1:
    print(f"{n} is a unity number.")
elif count == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is a composite number.")

                          #or

n = int(input("Give your number(to check if it's prime): "))

for i in range(2,n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")

