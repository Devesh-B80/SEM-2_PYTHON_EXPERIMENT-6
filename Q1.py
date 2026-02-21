"""Write a Python function to find the maximum and minimum numbers from a sequence 
of numbers.  (Note: Do not use built-in functions.)"""
# Function to find maximum and minimum from a sequence
# (without using built-in functions like max() or min())

def find_max_min(numbers):
    # Assume first element is both max and min initially
    maximum = numbers[0]
    minimum = numbers[0]

    # Traverse the sequence starting from second element
    for num in numbers[1:]:
        # Check for new maximum
        if num > maximum:
            maximum = num

        # Check for new minimum
        if num < minimum:
            minimum = num

    # Return both values
    return maximum, minimum


# -------- Main Program --------

# Take input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Call the function
max_val, min_val = find_max_min(nums)

# Display results
print("Maximum number:", max_val)
print("Minimum number:", min_val)