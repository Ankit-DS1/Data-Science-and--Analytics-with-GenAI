#1.Print unique Elements in a Array
  #Display all distinct elements present in the given array.

a = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,8,8,8,9,9]
 
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d.keys())

#2.Count Frequency of Array Elements
    #Count how many times each element appears using. a dictionary or hash map.


a = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,8,8,8,9,9]
 
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

#3.LeetCode 771 - Jewels and Stones
    #Count how many stones are also jewels based on given strings.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for i in S:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        count = 0

        for i in d.keys():
            if i in J:
                count += d[i]

        print(count)

#4.LeetCode 1832 - Pangram check
    #Verify if a sentence contains every letter of the English alphabet at least once.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for i in sentence:
            if i in d.key():
                d[i] += 1
            else:
                d[i] = 1
        
        if len(d.keys()) == 26:
            return True
        else:
            return False
        
#5.LeetCode 2351 - First Letter to Appear Twice
    #Find the first character that appears twice in a string.

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d.keys():
                return i
            else:
                d[i] = 1
        
#6.LeetCode 1748 - Sum of Unique Elements
    #Return the sum of elements that appear exactly once in the array.

class solution:
    def sumofUnique(self, nums: list[int]) -> int:
       d = {}
       for i in nums:
           if i in d.key():
               d[i] += 1
           else:
               d[i] = 1
        
       sum = 0
       for i in d:
           if d[i] == 1:
               sum = sum + 1

       return sum     

#7.Leetcode 2418 - sort the people
   #sort names of people based on their heights in descending order.

#class solution:
#   def sortpeople(self, names: List[str], heights: List[int]) -> List[str]:
#       d = {}
#       for i in range(len(names)):
#         d[heights[i]] = names[i]

#          d = sorted(d.items(), key=lambda x: x[0], reverse=True)
#
#          for i in range(len(d)):
#             names[i] = d[i][1]
            
#          print(names)



#8.Check if two string Have same Frequency Map
   #Compare character frequencies of two string appears in the second string.

s1 = "aabbcc"
s2 = "baccab"

d = {}

if len(s1) == len(s2):
    d = {}
    for i in s1:
        if i in d.key():
            d[i] += 1
        else:
            d[i] = 1
        
    for i in s2:
        if i in d.keys():
            d[i] -= 1
        else:
            print("An Extra element was found")
    
    for i in d:
        if d[i] != 0:
            print("Sorry your elements are not same")
            break
        else:
            print("Your string are same")
else:
    print("Not same")

#9.Find Duplicates in Array using Hashset
   # Detect and print elements that appear more than once in tha array.

a = [1,1,2,2,3,3,4,4,5,5,6,6,6,7,8]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d:
    if d[i] > 1:
        print(i)

#10.Leetcode 2404 - Most Frequent Even Element
   #Find the even number with the highest frequency; return the smallest one if ties exist.

#class solution:
#    def mostfrequentEven(self, nums: List[int]) -> int:
#        d = {}

#       for i in nums:
#            if i % 2 == 0:
#                if i in d.keys():
#                    d[i] += 1
#                else:
#                    d[i] = 1
        
#        if not d:
#            return -1
        
#        max_f = max(d.values())

#        cand = [num for num , freq in d.items() if freq == max_f]

#       print(min(cand))

#


#11.Leetcode 2283 - check if number has equal digits count and digit value
  # Determine if the count of each digits matches its calue in the string.



#12.Intersection of two Arrays
  #  Return all unique elements that appear in both aarays.


a = [1,2,2,1]
b = [2,2,3,3]

j = []
d = {}
for i in a:
    if i in d.key():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys():
    if i in b:
        j.append(i)

print(j)







    




    
           
        
    
       



               
   
         
        
               
