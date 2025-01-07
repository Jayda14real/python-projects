# Compile errors vs Run time errors
from colorsys import yiq_to_rgb

# SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# print(5+7)
# print("hello)
# def calculator():
#     pass
# NameError: This exception is raised when a variable or function name is not found in the current scope.
# print(a)

# TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
#print("Hello"+5)


# ValueError:This exception is raised when a function or method is called with an invalid argument or input.
# int("g")


# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
# a = 5
# b = 0
# print(a/b)
#############################################


# x= 5
# y= "7"
# z= x+y
# print(z)
# print("Goodbye")

#Exception Trapping
##############################################
# try:
#   x = 5
#   y = int(input("Give me an integer "))
#   z = x + y
#   print(z)
# except Exception: # The basic way
#   print("Error: cannot add an int and a str")
#   #pass
#
# print("Goodbye")


###########################################
# x=5
# y="Hello"

# try: 
#   z = x + y 
#   print(z)
# except TypeError: 
#   print("Error: cannot add an int and a str") 

# print("Goodbye")

#############################################
# x = 5
# y = "hello"
#
# #z = x + y
# try:
#     z = x + y
#     print(z)
# except TypeError as e:
#     print("Error: cannot an an int and a str")
###############################################

# Program to handle multiple errors with one 
# except statement 

# def fun(a):
# 	if a < 4:
# 	 b = a/(a-3)
# 	print("Value of b = ", b)
#
#
# try:
#   fun(5)
# except ZeroDivisionError:
# 	print("Cannot divide by zero - a cannot be 3")
# except NameError:
# 	print("NameError Occurred")

############################
# Create an input function
# Prompt for a positive intger
# Anticipate what could go wrong
# Raise exceptions

# def inputnum():
#   try:
#     num = input("Please enter a positive integer ")
#     num = int(num)
#   except ValueError:
#     print("That was not an integer")
#     raise
#   except:
#     raise
#   else:
#     if num <=0:
#       print("That was not a positive integer")
#     return num
#
# try:
#   num = inputnum()
#   print(num)
# except Exception as error:
#   print(error)

#############################################
Better option

# def inputnum():
#   try:
#     num = input("Please enter a positive integer ")
#     num = int(num)
#   except ValueError:
#     raise Exception("That was not an integer")
#   except:
#     raise
#   else:
#     if num <=0:
#       raise Exception("That was not a positive intger")
#     return num
#
# try:
#   num = inputnum()
#   print(num)
# except Exception as error:
#   print(error)