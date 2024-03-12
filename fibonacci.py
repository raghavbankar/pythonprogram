def print_fib(n):
    if n < 1:
        print("Invalid Number of terms")
        return
 
    # When number of terms is greater than 0
    prev1 = 1
    prev2 = 0
 
    # For loop to print Fibonacci series
    for i in range(1, n + 1):
        if i > 2:
            num = prev1 + prev2
            prev2 = prev1
            prev1 = num
            print(num, end=" ")
 
        # For first two terms
        if i == 1:
            print(prev2, end=" ")
        if i == 2:
            print(prev1, end=" ")
 
n=int(input("Enter a number "))
 
# Function Call
print_fib(n)