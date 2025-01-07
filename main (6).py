# Exploring Print function a bit more

a = 5

b = 5.4
c = "abc"

# print(a+3)

# print(f"My number is {a}")
#
# print("My number is",a, 7.5)
# print(a,b)

# print(a,c)

#print(a,9,b,"are we getting it?",c)

# Effiecient printing
# print(a,b,c)
# print(a,"\n",b,"\n",c)
# #
# print(a,"\n",b,"\n",c,sep="")
# print(1,2,3)
# print(1,2,3,sep= "")
#
# print(a,b,c)#
print(a,b,c,sep=";")
# #
# print(a,b,c,sep="?"*10)
# #
# print(a,b,c,sep="\n")

# for formatting a date
# print("09","11","2023", sep="/")
#
# # # #another example
# print("nadun","msmary", sep="@")


# Create the following using print

# ********************
# print("*"*20)

# How about this?

# ********************
# ********************
# ********************

# print("*"*20,"*"*20,"*"*20, sep = "\n")

# and this?

# *
# **
# ***
# ****
# *****

# print("*", "*"*2, "*"*3, "*"*4, "*"*5, sep = "\n")

########################################################################################################################

# Question 01
# Create the following output using print()
# There are 20 - and 5 |
# You may use only MAXIMUM of 5 print commands

# |--------------------|
# |                    |
# |                    |
# |                    |
# |--------------------|

print("|", "-"*20,'|',sep="")
print("|"," "*20,'|', sep="")
print("|"," "*20,'|', sep="")
print("|"," "*20,'|', sep="")
print("|", "-"*20,'|',sep="")
# Question 2

# Write a program that accepts an integer (n) and prints on one line the value  of n, the value of n*n, the value of n*n*n, and the sum of all 3 of those values. The print statements each separated by three dashes, like below. The sep argument may prove useful.

# If for instance the input is 15, you should have python print

# 15---225---3375---3615

# Hint: You should make Python calculate all the numbers based on the input - do not calculate anything by yourself.

# Question 3

# Write a program that accepts base and height of a triangle, and calculates the area. Try to use ONLY 1 print statement to accomplish output shown. You should make python round the answer to one decimal place.


# For triangle with base 5.2 and height 4.3 the area is 11.2.

#Hint: The formula to calculate the area of a triangle is area= 0.5*base*height