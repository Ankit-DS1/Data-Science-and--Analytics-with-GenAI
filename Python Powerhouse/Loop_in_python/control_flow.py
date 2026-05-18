                      #class 7

#Loops in python

#for loop
#syntax
#for variable in sequence:
    #code to be executed
#example
for i in range(5):
    print(i)

#while loop
#syntax
#while condition:
    #code to be executed
#example
i = 0
while i < 5:
    print(i)
    i += 1
 
 #do while loop
#python does not have a built-in do while loop, but we can simulate it using a while loop and a flag variable 

#for loop

ran = range(1,10,1)

for i in ran:
    print(i)

    #or

for i in range(1,10,1):
    print(i)

for i in range(35,4,-1):
    print(i)


#table of 5 

for i  in range(5,51,5):
    print(i)

#table of n

n = int(input("Enter a number you want the table of: "))

for i in range(n,(n *10)+1,n):
    print(i)

#loop in string 

name = "python powerhouse"
for i in name:
    print(i)

for i in range(0,len(name),1):
    print(name[i])

a = "python powerhouse"
for i in range(len(a)):
    print(a[i])

