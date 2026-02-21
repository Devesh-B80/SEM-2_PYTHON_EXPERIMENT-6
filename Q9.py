""" Write a program to create two lists and generate a dictionary with keys from list1 and 
values from list2."""
# Program to create a dictionary using keys from list1 and values from list2

# Take number of elements
n = int(input("Enter number of elements: "))

# Initialize lists
list1 = []
list2 = []

print("Enter elements for list1 (keys):")
for _ in range(n):
    list1.append(input())

print("Enter elements for list2 (values):")
for _ in range(n):
    list2.append(input())

# Create dictionary using zip()
result_dict = dict(zip(list1, list2))

# Display result
print("Generated Dictionary:", result_dict)