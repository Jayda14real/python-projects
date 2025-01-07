# Review

#Problem 01
# Create a function that takes month as an integer parameter, and returns month as a 3 character string:
#Example

# print(monthName(3))
# print(monthName(8))
# print(monthName(14))
# Mar
# Aug
# Invalid month



##########################################

size = input("What is the size of the pizza?")

pep = input("Do you need extra pepperoni? Y or N?")

if ((size == 's') or (size == 'm')) and pep == 'Y':

    price = 15
else:

    price = 10

print(price)





# Create a function that sums 2 integer values. If the sum is between 25 and 30, return the value 30. Otherwise, return the sum.

# There are 3 ways we can go about this.



#Version 1
# def sum2_val(a,b):
#
#     sum = a+b
#
#     if 25<= sum <=30:
#
#         sum = 30
#
#     return sum


#Version 2
# def sum2_val(a,b):
#
#     sum = a+b
#
#     if (sum >=25) and (sum <=30):
#
#         sum = 30
#
#     return sum
#
# ans = sum2_val(a = 17,b = 12)
#
# print(ans)


# DeMorgan's laws

# print(True,True,not(True and True),not True or not True)

# print(True,False,not(True and False),not True or not False)

# print(False,True,not(False and True),not False or not True)

# print(False,False,not(False and False),not False or not False)

# print(True,True,not(True or True),not True and not True)

# print(True,False,not(True or False),not True and not False)

# print(False,True,not(False or True),not False and not True)

# print(False,False,not(False or False),not False and not False)

# a = "Testing"
# if not (type(a) == int or type(a) == float):
#   print("a is neither an integer nor a float")

# if type(a) != int and type(a) != float:
#   print("a is neither an integer nor a float")

# Need order to evaluate conditions
# PEMDAS first
# Conditionals (> , <, ==, in, etc)
# not
# and
# or
# Use () to clarify


# Write a code if a and b both greater than 0 then print both positive, or print bummer otherwise.

# a=-5
# b=6



# Short circuit logic

# a = -5
# b = 5
# if a > 0 and b > 0:
#   print("Both a and b are positive")

# a = 5
# b = 5 * 5 - 75 / 3
#
# if a > 0 and b != 0 and a / b > 0:
#     print("Something")
# else:
#     print("Values were not as expected")