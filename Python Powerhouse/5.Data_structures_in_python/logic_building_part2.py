#1.Linear Search 
  #search for a given element by checking each element one by one.

a = [1,2,3,4,5,45,667,89,0,2234,56,78,6,54,334,5]
search = 6

for i in range(len(a)):
    if a[i] == search:
        print(f"Element found at index {i}")
        break
else:
    print("Element not found in the list.")


#2.Binary Search
    #Effixient search for an element in a sorted list using the divide-and-conquer approach.

a = [1,2,3,4,5,10,24,34,56,78,89,90,100]
search = 34

start = 0
last = len(a) - 1
mid = (start + last) // 2
while start <= last:
    if a[mid] == search:
        print(f"Element found at index {mid}")
        break
    elif a[mid] < search:
        start = mid + 1 
        mid = (start + last) // 2

    elif a[mid] > search:
        last = mid - 1
        mid = (start + last) // 2

else:
    print("Element not found in the list.")

#3. Bubble Sort
    #Sort the list by repeatedly swapping adjacent elements if they are in the wrong order.

a = [64, 34, 25, 12, 22, 11, 90]

for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)

#4.Selection Sort
    #Sort the list selecting the smallest element in each pass and placing it in the correct position.

a = [64, 25, 12, 22, 11]

for i in range(len(a)-1):
    j = i + 1
    min - i
    for k in range(j, len(a)):
        if a[k] < a[min]:
            min = k
    a[i], a[min] = a[min], a[i]

print(a)


