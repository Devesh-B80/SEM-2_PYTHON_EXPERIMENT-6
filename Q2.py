"""Write a Python function that takes a positive integer and returns the sum of the cube of 
all the positive integers smaller than the specified number. 
"""
# Function to return sum of cubes of all positive integers less than n

def sum_of_cubes(n):
    total = 0  # variable to store the sum

    # Loop from 1 to n-1
    for i in range(1, n):
        total += i ** 3  # add cube of i

    return total


# -------- Main Program --------

# Take input from user
num = int(input("Enter a positive integer: "))

# Call the function and print result
result = sum_of_cubes(num)
print("Sum of cubes:", result)