num=int(input("Enter a number to print a pattern"))
for i in range(1,num+1,1):
    for j in range(1,num+1,1):
        if(j<=i):
            print(i,end="")

    print("\r")