num= int(input("Enter a number"))
def sumofdigits(num):
    
    digit=0
    while(num!=0):
        digit+=num%10
        num=int(num/10)

    print(digit)

sumofdigits(num)

 
    

    