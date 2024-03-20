# Given an array of size n. The task is to rotate array by d elements where d ≤ n.

def rotate(arr, d):
    for i in range(d):
        arr.append(arr.pop(0))
    return arr

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(arr)
    print(rotate(arr, 3))

if __name__=='__main__':
    main()