list=[1,2,3,67,32,45,88]
num=int(input("Enter a number of which the divisibility need to be find"))
list1=[]
for i in range(len(list)):

    if(list[i]%num==0):
        print(list[i])
    

