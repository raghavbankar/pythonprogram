num=int(input("Enter a number to print a pattern"))
for i in range(num):
    for j in range(num+2):
        
        
        if(i<=num-1 & j<=num-1):
            print(" ")
        else:
            print("*",end="")

    print("\r")          


