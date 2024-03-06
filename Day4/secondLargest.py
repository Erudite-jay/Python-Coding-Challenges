# https://www.geeksforgeeks.org/problems/second-largest3735/1
# Given an array Arr of size N, print 
# the second largest distinct element from an array. If the second largest element doesn't exist then return -1.


li=[10,20,30,40,120,60,70,80,120]

# method 1 -> using inbuilt function of list and removing that largest element and than again finding maximum element

# max1=max(li)
# li.remove(max1)
# max2=max(li)
# print(max2)

# method 2 -> Sort the list and then convert into set and the return last second element

# method 3  -> using logical approach 
 
max1= li[0]
max2= li[0]

for i in range(0,len(li)):
    if li[i] > max1: 
        max2= max1
        max1= li[i]
    elif li[i]!=max1 and li[i]>max2:
        max2= li[i]

print(max2)