"""Write functions to explain the mentioned concepts: 
a. Keyword argument 
b. Default argument 
c. Variable-length argument """
# Function demonstrating keyword arguments
def student_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Calling function using keyword arguments
student_info(age=20, city="Dehradun", name="Rahul")