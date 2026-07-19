#1.Sum & Average of a list
   #create a list of numbers,then calculate and print the total sum and average.

a = [10, 20, 30, 40, 50]
sum = 0

for i in a:
    sum += i

print(f"Sum: {sum}")
print(f"Average: {sum / len(a)}")

#2.Maximum Element with index
   #find the largest element in the list along with its position(index).

a = [10, 20, 30, 40, 50,23,456,86,44,356,7,88]

max = a[0]
index = 0

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        index = i

print(f"your maximum element is {max} at index {index}")

#3.Second Greatest Element 
    #Identify the second largest element in the list without sorting directly.



a = [10, 20, 30, 40, 50,23,456,86,44,356,7,88]

max = a[0]
max2 = a[0]
index = 0
index2 = 0

for i in range(len(a)):
    if a[i] > max:
        max2 = max
        max = a[i]
        index2 = index
        index = i
    elif a[i] > max2:
        max2 = a[i]
        index2 = i

print(f"your second maximum element is {max2} at index {index2}")

#4.Check if list is sorted(increasing)
    #verify whether the list elements are in ascending order.

a = [10,20,30,40,50,60,70,80,90]

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")

#5.Left Rotation by 1
   #shift all elements one position to the left, with the first element moving to the end.

a = [10,20,30,40,50]

for i in range(len(a)-1):
    a[1],a[i+1] = a[i+1],a[1]

print(a)

#6.Left rotation by k
    #Generalize the previous problem: rotate the list k times to the left.

k = int(input("Enter the number of rotations: "))
a = [10,20,30,40,50]

for i in range(k):
    a[1],a[i+1] = a[i+1],a[1]

print(a)

#7.Reverse list(in place)
    #Reverse the entire list without using extra space(i.e swap elements).

a = [10,20,30,40,50]

b = len(a)-1

for i in range(len(a)//2):
    a[i],a[b] = a[b],a[i]
    b -= 1

print(a)