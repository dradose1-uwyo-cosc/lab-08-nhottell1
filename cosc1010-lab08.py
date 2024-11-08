# Nolan Hottell
# UWYO COSC 1010
# 11-07-24
# Lab 8
# Lab Section:13
# Sources, people worked with, help given to: Bradley Ekstrom, Riley Green, Internet
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 



import math


print("*" * 75)


def convert_to_number(s):
   try:
       if '.' not in s:
           return int(s)
       elif s.count('.') == 1:
           return float(s)
   except ValueError:
       return False
   return False


def slope_intercept(m, b, lower, upper):
   if not isinstance(lower, int) or not isinstance(upper, int):
       return False
   if lower > upper:
       return False
   y_values = []
   for x in range(lower, upper, + 1):
       y = m * x + b
       y_values.append(y)
   return y_values


while True:
   m = input('Enter the slope (m), or "exit" to quit ')
   if m.lower() == 'exit':
       break
   b = input("Enter the y-intercept (b)? ")
   lower = input("What is your lower bound? ")
   upper = input("What is your upper bound? ")


   m = convert_to_number(m)
   b = convert_to_number(b)
   lower = convert_to_number(lower)
   upper = convert_to_number(upper)


   if m is not False and b is not False and isinstance(lower, int) and isinstance(upper, int):
       result = slope_intercept(m, b, lower, upper)
       print(f"Resulting y value for the given x range: {result}")
   else:
       print("Invalid input. Please enter a valid number.")
print("*" * 75)


def safe_sqrt(x):
   if x < 0:
       return None
   return math.sqrt(x)


def quadradic_function(a, b, c):
   x = b**2 - 4 * a * c
   sqrt_x = safe_sqrt(x)
   if sqrt_x is None:
       return None
  
   root_1 = (-b + sqrt_x) / (2 * a)
   root_2 = (-b - sqrt_x) / (2 * a)
   return root_1, root_2


while True:
   a = input("Enter coefficient a, or 'exit' to quit: ")
   if a.lower() == 'exit':
       break
   b = input("Enter coefficient b: ")
   c = input("Enter coefficient c: ")


   a = convert_to_number(a)
   b = convert_to_number(b)
   c = convert_to_number(c)


   if a is not False and b is not False and c is not False:
       result = quadradic_function(a, b, c)
       if result is None:
           print("No real roots")
       else:
           print(f"The roots are: {result}")
   else:
       print("Invalid input. Please other numbers.")



    



# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
