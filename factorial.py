num=int(input("Enter a num to find its factorial"))

i=num
fact=1
while i>1:
    fact*=i
    i-=1
print(fact)