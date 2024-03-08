# https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

# check an array is sorted or not 

def checkSortedArray(l1):
      for i in range(len(l1)-1):
          if l1[i]>l1[i+1]:
              return False
      return True

def main():
    l1=[10,20,22,21,70,80,90,100]
    print(checkSortedArray(l1))

if __name__ == "__main__":
    main()