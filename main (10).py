from os.path import basename


# Creating your own functions

# def new_function():
#
#   print("This is a new function")
#
# new_function()

# x = 5
#
# def x():
#   print("Something")
# print(x)
#
# print(type(x))


# x()


# Create a function to add/subtract numbers

# Functions with inputs
# def calculator(a,b):
#     c = a + b
#     d = a - b
#     print(f"a + b is {c} and a - b is {d}")
#
#
# calculator(a = 19, b = 15)

#####################################################
# Question 01

# Create a function to do the following
# Name the function calcVals
# Generate two random integers between 1 and 100 (one at a time) and save them in variables called a and b
# Calculate sum, difference, product, remainder for a and b
# Print results on one line
# Test your function

# import random
#
# def calcVals():
#
#     a = random.randint(a = 1,b = 100)
#     b = random.randint(a = 1,b = 100)
#     print(a+b,a-b,a*b,a%b)
#
# calcVals()

############################################################################################

# Function arguments

# def greet(name):
#   print(f"Hello {name}")
#   print(f"How are you doing {name}?")

#greet("Nadun")

###############################################################################################

# Question 02
# Create a function to do the following
# Name the function calcSum()
# Pass 2 values to our function a and b
# Calculate sum for a and b
# Print results of our function

# def calcsum(a,b):
#
#     print(a+b)
#
# calcsum(a = 1, b = 2)





# Question 03
# Create a function to do the following
# Name the function calcDiff()
# Pass 2 values to our function a and b
# Calculate difference of b from a
# Print results of our function

# def calcDiff(a,b):
#
#     print(a-b)
#
# calcDiff(a = 1, b = 2)




###################################################################################################

# Question 04

#Create function that prompts user for the base and height of a triangle, calculates the area, and prints the result.
# There should be seperate functions for user inputs and calculations.

# Mondays work
# def area_triangle(base,height):
#
#     area = 0.5 * base * height
#     print(f"The area of the triangle is {area}")
#
# area_triangle(base = 10, height = 20)


# Wednesdays work

x = 8 #Global Variable

b = float(input("What is the base?"))
h = float(input("What is the height?"))

def area_triangle(base,height):

    area = 0.5 * base * height

    return area

area_tri = area_triangle(b,h)

print(f"The area of the triangle is {area_tri}")


