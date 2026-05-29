# While Loop

# Syntax of while loop

# while condition:
#     # code to be executed

# Example of while loop
#1


i = 1
while i <= 5:
    print(i)
    i = i + 1

#2
j = 10

while j >= 0:
    print(j)
    j = j - 1

#3

for i in range(1, 11):
    print(i)
    if i == 5:
        break

a = 1
while a <= 10:
    print(a)
    a = a + 1
    if a == 5:
        break

for i in range(1, 5):
    if i == 8:
        continue
    print(i)
else:
    print("Loop is completed without break")

