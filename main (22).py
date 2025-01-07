# Indefinite Loops


# Problem 01
# Write a code where you ask any two integers from the user as long as the sum of the two integers are less than zero.
# Each time print the ratio of two numbers (first divided by the second).
# However, if user's second number is zero stop the program.

# num1 = int(input("Tell me an integer?"))
# num2 = int(input("Tell me another integer?"))
#
# sum = num1 + num2
#
#
# while sum < 0:
#     if num2 == 0:
#         break
#     else:
#         print(num1/num2)
#
#     num1 = int(input("Tell me an integer?"))
#     num2 = int(input("Tell me another integer?"))
#
#     sum = num1 + num2

Temp = True


while Temp:

    num1 = int(input("Tell me an integer?"))
    num2 = int(input("Tell me another integer?"))

    sum = num1 + num2

    if sum > 0:

        Temp = False
        #break

    elif num2 == 0:
        #Temp = False
        break

    else:
        print(num1/num2)

# Problem 02
# Go through the following list - print out each integer in the list one at a time until you come across a string - don't print the string. 

# lst=[5,9,11,21,67,81,"t",8,0]


# Problem 03

# Write a program where you get a number from the user between 1 and 100 and keep subtracting 3 from it until the number becomes negative.

# num=int(input("Tell me a number between 1 and 100 "))
#
# while num >= 0:
#
#     num -= 3
#     print(num)

# Problem 04

# Write a program for a guessing game. The computer generates a random number between 1 and 10 and user has to guess the number within 5 attempts. Code up the game!

