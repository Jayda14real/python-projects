
# Random Package
import random
# Generating a random integer

# print(random.randint(30,70))

# Generating a random float between 0 and 1

# print(random.random())

# Generating a random number (float) between a and b

#a + random.random() * (b-a)

# print(random.random()*10)
# print(random.random()*(60-20) + 20)

# Random choice from a given collection

# print(random.choice("abcdefghijklmnopqrstuvwxyz"))
# print(random.choice((4,5,6,2,3,9,10)))

# Random choices (plural)

# print(random.sample("abcdefghijklmnopqrstuvwxyz",3))

# Seed - pseudorandom number generators

#random.seed(2)
#print(random.randint(10,20))

###############################################################################################

## Quiz Problems

# Question 01

# Use the math library to find sin(80)
# Use the math library to find what 7^(0.845)

# Import Math Library
# import math
# print(math.sin(80))


# Question 02

# Generate a random integer between 37 and 75
# Generate a random number between 30 and 70. What would you add to the code so that everytime you and I (Nadun) run your code
# we get the same random number?

# random.seed(2)
# print(random.randint(37,75))


# Question 03

# Write a program where you ask the user for their name and randomly pick a letter from their name. Print the letter to teh console.

name = input("Hello what is your name?")
random_letters = name""

# # Question 04

# Write a program for a game where you throw a dice. Your program should first ask for user's name and greet them as "Greetings NAME ".
# Then use the random library to simulate throwing a dice and print the result to the console. Your final result should be a statement like:
# "Hello, NAME, you threw X"

# name = input("Hello, what is your name?")
# print(f"Grettings {name}, roll the die")






# Question 05

# Write a program where you prompt the user to enter the radius of a circle they know. Using that, find the area and the circumference and print them as:

# "The area and circumference of a circle with radis R is A and C"

# Formulas: Area = pi*R^2 and Circumference = 2*pi*r