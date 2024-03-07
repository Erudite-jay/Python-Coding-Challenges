# Given an array of N integers, and an integer K, 
# find the number of pairs of elements in the array whose sum is equal to K.

# method 1--> with O(n) time and O(n) space
k=6
l1=[1,5,7,1]
s ={}
count = 0
for i in l1:
     if i in s:
         s[i] +=1
     else:
         s[i] = 1 

     if k-i in s:
      count=count+s[k-i]
print(s)     
print(count)

