# 1.Find the year whether it's LEAP Year / OR NOT

yr = int (input("Enter year to check leap year"))

if (yr%400==0 or (yr%4==0 and yr%100!=0)):
    print("Leap year")
else:
    print("Not a leap year")


#another Solution using nested loops
    
if (yr%400==0):
    print("Leap year")
elif (yr%100)!=0:
    if (yr%4==0):
        print("Leap year")
    else:
        print("Not a leap year")
 