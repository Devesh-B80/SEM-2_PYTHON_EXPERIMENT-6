"""Write a lambda function to find volume of cone."""
# Lambda function to calculate volume of a cone
volume_cone = lambda r, h: (1/3) * 3.14159 * r**2 * h

# -------- Main Program --------

# Take input from user
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

# Calculate and display volume
print("Volume of cone:", volume_cone(radius, height))