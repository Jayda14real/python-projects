
# Question 01

# Add the value "testing" to end of list L
# [’some’, 3, 4, ’values’, 7, 10]


# Question 02

# Write a Python program. Find all even integers in the list and delete them
# [8, 4, 5, 12, ’cat’, ’bird’]

#Question 03. Given below is a list of incomes of several folks:

# I=[127000,95000,156000,30000,75000,109000,44000]

# Sort the income list and calculate their federal tax according to 2024 tax brackets. 



######################################

#List comprehension

# L = [i for i in range(10)]
# print(L)

# L = [i**2 for i in range(10)]
# print(L)

# L = [i*2 for i in range(7)]
# print(L)


# import random
# L = [random.randint(1,100) for i in range(10)]
# print(L)

# L=[4,8,9,20]
# N = [2*i for i in L]
# print(N)

# Increase the values in teh following list by 20% and save in a new list

# L=[1000,2000,500,4000]
#
# new_L = [salary*1.20 for salary in L]
#
# print(new_L)

# Create a new list that consist of numbers between 30 and 35 from the following list

# L = [30, 15, 32, 27, 38, 33]

# new_L = []
#
# for num in L:
#
#     if 30 <= num <= 35:
#
#         new_L.append(num)
#
# print(new_L)

# new_L = [num for num in L if 30 <= num <= 35]

# print(new_L)

# Given a list of numbers, create a new list with just odd numbers from the list:

numbers = [3,5,45,97,32,22,10,19,39,43]

# Odd = []
#
# for num in numbers:
#
#     if num % 2 !=0:
#
#         Odd.append(num)
#
#     else:
#
#         Odd.append(0)

# Odd = [num for num in numbers if num % 2 !=0]

# Odd = [num if num % 2 !=0 else 0 for num in numbers]
# print(Odd)

L = ['even' if i % 2 == 0 else 'odd' for i in range(1,11)]

print(L)





