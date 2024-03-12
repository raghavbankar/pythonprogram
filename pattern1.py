num=int(input("Enter a number to print a pattern"))
for i in range(num):
    for j in range(num):
        if(j<=i):
            print("*",end="")

    print("\r")          

print("\r")

for i in range(num):
    for j in range(num):
        if(i<=j):
            print("*",end="")

    print("\r")          

