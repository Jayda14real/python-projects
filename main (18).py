
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# Name 1	Name 2	Score
# Catherine Zeta-Jones     	Michael Douglas    	99
# Brad Pitt  Jennifer Aniston	73
# Prince William	Kate Middleton	67
# Kanye West	Kim Kardashian	42
# Beyonce	Jay-Z	23

#HINTS:

# 1. The lower() function changes all the letters in a string to lowercase.

# 2. The count() function will give you the number of times a letter occurs in a string.

# name = 'Jaden'.lower
# print(name)
# print(name.count('J'))


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#True
name1 and name2.count('t')
name1 and name2.count('r')
name1 and name2.count('u')
name1 and name2.count('e')

#Love
name1 and name2.count('l')
name1 and name2.count('o')
name1 and name2.count('v')
name1 and name2.count('e')














