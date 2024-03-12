
temp=int(input("Enter a Number"))

sum1=0
while(temp!=0):
        r = temp % 10
        sum1 = sum1 + r**3
        temp = temp/10

if(temp==sum1):
    print("The number is armstrong")
else:
    print("The number is not a srmstrong")