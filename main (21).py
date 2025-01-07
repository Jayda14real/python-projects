#Question 01
# Consider the given list of numbers. Print only the numbers which are divisible by 5.
# L=[10,3,9,15,25,41,65]
#
# for num in L:
#
#     if num % 5 == 0:
#         print(num)


# Question 02
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# fruits=["banana", "orange", "mango", "lemon"]
#
#
# new_fruits = []
#
# for i in range(3,-1,-1):
#     new_fruits.append(fruits[i])
#
#
# print(new_fruits)


# Indefinite Loops

# for i in range(1,6):
#   print(i)



# n = 5
#
# while n > 0:
#   print(n)
#   n += 1



# print("Boom!!!")

# Write a code where you calculate the sum of numbers until the user enters zero.

# num = int(input("Give me an integer?"))
# sum = 0
#
# while num != 0:
#
#     sum += num
#     num = int(input("Give me an integer?"))
#
# print(sum)


# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.


# Using a while loop and an if statement write a code which appends all the elements in a list to a new list unless the element is an empty string: ""

list=["Jane","Jim","Nadun","Ann","","Tom","Joe"]

new_list = []

#For loop solution
# for item in list:
#
#     if item != "":
#         new_list.append(item)
#
# print(new_list)

#While loop solution
i = 0

while list[i] != "":

    new_list.append(list[i])
    i += 1

print(new_list)







