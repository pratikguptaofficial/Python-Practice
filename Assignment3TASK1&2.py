# Function to calculate factorial
#def factorial(n):
 #   if n == 0 or n == 1:
  #      return 1
   # else:
    #    return n * factorial(n - 1)  # recursion

# Taking user input
# num = int(input("Enter a number: "))

# Calculating and displaying result
# result = factorial(num)
# print(f"Factorial of {num} is: {result}")

import math

# Step 1: Ask the user for input
num = float(input("Enter a number: "))

# Step 2: Calculate required values using math module
square_root = math.sqrt(num)
natural_log = math.log(num)  # log base e
sine_value = math.sin(num)   # in radians

# Step 3: Display results
print(f"Square root of {num} is: {square_root}")
print(f"Natural log of {num} is: {natural_log}")
print(f"Sine of {num} (in radians) is: {sine_value}")





