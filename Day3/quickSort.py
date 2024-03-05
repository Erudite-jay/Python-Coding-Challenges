def main():
    l1=[10,20,40,22,45,9,-23909]
    print(l1)
    quickSort(l1,0,len(l1)-1)
    print(l1)

def quickSort(l1,low,high):
    if low<high:
        pi_idx = partition(l1,low,high)
        quickSort(l1,low,pi_idx-1)
        quickSort(l1,pi_idx+1,high)

def partition(l1,low,high):
    pivot=l1[high]
    i=low-1
    for j in range(low,high):
        if l1[j]<pivot:
            i=i+1
            l1[i],l1[j]=l1[j],l1[i]
    l1[i+1],l1[high]=l1[high],l1[i+1]
    return i+1

main()