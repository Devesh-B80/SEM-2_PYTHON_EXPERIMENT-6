"""Write a lambda function which gives tuple of max and min from a list. 
Sample input: [10, 6, 8, 90, 12, 56] 
Sample output: (90,6)"""
# Lambda function to return (max, min) from a list

max_min = lambda lst: (max(lst), min(lst))

# -------- Main Program --------

# Sample input (you can also take user input)
numbers = [10, 6, 8, 90, 12, 56]

# Call lambda
result = max_min(numbers)

# Display result
print(result)