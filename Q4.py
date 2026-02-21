"""Write a recursive function to print Fibonacci series upto n terms."""
# Recursive function to compute nth Fibonacci number
def fib(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fib(n - 1) + fib(n - 2)


# -------- Main Program --------

# Take number of terms
n = int(input("Enter number of terms: "))

print("Fibonacci series:")

# Print first n Fibonacci numbers
for i in range(n):
    print(fib(i), end=" ")