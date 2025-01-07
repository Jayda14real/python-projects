# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is $10 per item.
# If you buy 100 or more items, the cost is $7 per item. Write a program that prompts the user for how many items they are buying and prints the total cost.
# Once you have done it, add another feature where if they have a coupon, they get a $1 discount to the total.


# items = int(input("How many items are you buying today?"))
#
# coupon = input("Do you have a coupon? Y or N?")

# if items < 10:
#
#     cost = 12 * items
#
# elif 10 <= items <= 99:
#
#     cost = 10 * items
#
# else: #elif items >= 100
#
#     cost = 7 * items
#
#
# if coupon == "Y":
#
#     cost = cost - 1
#
# print(cost)

















# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.

# every year that is evenly divisible by 4 is a Leap year

# **except** every year that is evenly divisible by 100

# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇





















# Write a code to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    cost = 15

    if add_pepperoni == "S":
        cost = cost + 2

elif size == "M":
    cost = 20

    if add_pepperoni == "M":
        cost = cost + 3

elif size == "L":
    cost = 25

    if add_pepperoni == "L":
        cost = cost + 3

if extra_cheese
    cost = cost +1

print(cost)

