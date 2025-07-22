# user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # This will throw an error if num2 is 0

# print the results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# user to input first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate full name
full_name = first_name + " " + last_name

# Print personalized greeting
print(f"\nHello, {full_name}! Welcome to the Python program.")

