# Wap to check armstrong number

initial_n=input("Enter number to check for armstrong")

n_size=len(initial_n)
n=int(initial_n)

sum=0
for i in range(n_size):
    r=int(n%10)
    n=(n//10)
    sum=sum+r**n_size

if int(initial_n)==sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")