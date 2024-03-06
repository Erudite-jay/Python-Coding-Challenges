# Given a sorted array a[] of size n, delete all the duplicated elements from a[] & 
# modify the array such that only distinct elements should be present there.

# 1. Don't use set or HashMap to solve the problem.
# 2. You must return the modified array size where only distinct elements are present 

li=[1,2,2,4,4,4,4,10]

# method 1-> convert and return set length:
# print(len(set(li)))

# method 2 -> use iteration and count duplicate by comaparing present element with next one 
# count=0
# for i in range(0,len(li)-1):
#     if li[i]==li[i+1]:
#         count=count+1
# print(count)

# method 3-> remove duplicate elements-> return length of list
i=0
while(i<len(li)):
    if li[i-1]==li[i]:
        li.remove(li[i])
    else:
        i=i+1
print(li)
print(len(li))
