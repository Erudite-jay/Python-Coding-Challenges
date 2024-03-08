# https://www.geeksforgeeks.org/problems/pascal-triangle0652/1


# Method 1--->  Print pascal triangle 
# matrix = []
# def pascal_triangle(n):
#     for i in range(n):
#         li=[]
#         for j in range(i+1):
#             if i ==j or j == 0:
#                 li.append(1)
#             else:
#                 li.append(matrix[i-1][j-1]+matrix[i-1][j])
#         matrix.append(li)  

        
#     for row in matrix:
#         for col in row:
#             print(col, end=" ") 
#         print() 

# pascal_triangle(5)


# Method 2---> Return Particular Row using combination method

def nCr(n,col):
    ans=1
    for i in range(col):
        ans=ans*(n-i)
        ans=ans//(i+1)

    return ans

def pascal_row(n):
    li=[]
    for col in range(n):
         li.append(nCr(n-1,col))
    return li

print(pascal_row(5))