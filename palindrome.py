print("The palindrome from 500 to 1000 are")
for i in range(500,1000,1):
    num=str(i)
    if num == num[::-1]:
        print(num," ")
    
