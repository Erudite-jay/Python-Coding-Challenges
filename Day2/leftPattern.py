#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

n=int (input("Enter N"))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):    
        print("*",end=" ")  
    print()




# end=" " use
    
# When you use end=" ",
# you're specifying that you don't want anything (an empty string)
# to be printed at the end of the output. This effectively suppresses the default newline behavior of the print() function, 
# allowing you to print multiple items on the same line.
# Default is '\n' in end 

