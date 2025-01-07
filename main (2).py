# Wednesday Code

# Variables

# get the name from the user, calculate the length and print it

# print(len(input("What is your name?")))

# name = input("what is your name?")
# num_char = len(name) # This is where we calculate the length of the name
# print(num_char)




# Some questions to think?
# 1. Can two people have the same name?
# 2. Are variables case sensitive?
# 3. Can variables contain both letters and numbers?
# 4. Can contain _ ?
# 5. Can contain space?

# Good practice tips

# Long names increase typo risk
# Lower case letters for first letter
# Avoid _ for first letter, reserved for system

# Data type check - print the data types of the following

# txt = "This is a long string" # This is a string
# a = 5 # This is an integer
# b =31.7 # float
#
# print(type(b))

# Type errors

# What is the difference between len("hello") and len(1234) command?

# print(len("1000"))

#print(len("50"))

##############################################################################


name = input("what is your name? ")
num_char = len(name) # This is where we calculate the length of the name
# print("Your name has num_char characters")

# print("Your name has" + str(num_char) + "characters") #right

# print("Your name has" + "num_char" + "characters") #wrong

# print("Your name has" + " " + str(num_char) + " " + "characters") #better

print(f"Your name has {num_char} characters") #even better


# num_char= len(input("What is your name?"))
# print(type(num_char))
# print("Your name has" + num_char+ "characters.")


#print("tim"+100.5)


# length = float(input("what is the length?"))
#
# width = float(input("what is the width?"))
#
# area = length * width
#
# print(f"The area of the rectangle is {area}")


