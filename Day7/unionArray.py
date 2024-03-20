# Union of two arrays can be defined as the common and distinct elements in the two arrays.
# Given two sorted arrays of size n and m respectively, find their union.

# method 1 use set method -> convert into set and make union 
# def union(l1, l2):
#   return list(set(l1).union(set(l2)))


# method 2 -> using merge sort method
def union(l1, l2):
    i=0
    j=0
    res=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            if len(res)==0 or l1[i]!=res[-1]:
                res.append(l1[i])
            i+=1
        else:
            if len(res) == 0 or l2[j]!=res[-1]:
                res.append(l2[j])
            j+=1
    while i<len(l1):
        if l1[i]!=res[-1]:
            res.append(l1[i])
        i+=1
    while j<len(l2):
        if l2[j]!=res[-1]:
            res.append(l2[j])
        j+=1
    return res

def main():
    l1=[2, 2, 3, 4, 5]
    l2=[1, 1, 2, 3, 4]
    print(union(l1,l2))
    

if __name__ == '__main__':
    main()