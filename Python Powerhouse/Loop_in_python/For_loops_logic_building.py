
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

#4.sum of Ntuaral numbers
#Take input n and calculate the total sum from 1 to n.

n = int(input("Please enter a number: "))

s = 0
for i in range(1,n+1):
    s = s + i
print(f"The sum of first {n} natural numbers is: {s}")


