"""Write a program to check whether all the values in a dictionary are the same or not using 
a lambda function. """
# Lambda function to check whether all values in a dictionary are the same
all_same = lambda d: len(set(d.values())) == 1

# -------- Main Program --------

# Take number of key-value pairs
n = int(input("Enter number of items: "))

data = {}

print("Enter key-value pairs:")

# Input dictionary elements
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Check and display result
if all_same(data):
    print("All values are the same.")
else:
    print("Values are different.")