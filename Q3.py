""" Write a Python function to print 1 to n using recursion. (Note: Do not use loop) """
# Function to print numbers from 1 to n using recursion
def print_1_to_n(n):
    # Base case: stop when n becomes 0
    if n == 0:
        return

    # Recursive call first (go to smaller problem)
    print_1_to_n(n - 1)

    # Print after returning (ensures increasing order)
    print(n, end=" ")


# -------- Main Program --------

# Take input from user
num = int(input("Enter a positive integer: "))

# Call the recursive function
print_1_to_n(num)
