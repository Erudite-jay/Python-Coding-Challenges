# Move all the zero elements to end of the array

li=[1,4,0,0,0,20,2,4,0,0,2,0]

# method 1 -> it doesn't maintaiin the order of the non zero elements
# i=0
# j=len(li)-1
# while(i<j):
#     if li[i]==0:
#         li[j],li[i] =li[i],li[j]
#         j=j-1
#     else:
#         i=i+1

# print(li)

# method 2 -> While maintaining the order of non zero elements 
count_zero,i=0,0
while(i<len(li)-count_zero):
    if li[i]==0:
        li.pop(i)
        li.append(0)
        count_zero=count_zero+1
    else:
        i=i+1

print(li)