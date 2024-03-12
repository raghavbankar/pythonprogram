list=["p","q"]
n=int(input("Enter a number"))

new_list=['{}{}'.format(x,y) for y in range(1,n+1)for x in list]

print(new_list)
