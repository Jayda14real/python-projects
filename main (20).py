# You are going to write a program that calculates the highest score from a List of scores.

#Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0

for score in student_scores:

  if max_score < score:
    max_score = score


print(f"The highest score is {max_score}")

#################################

#You are going to write a program that calculates the average student height from a List of heights.

#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.


# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# print(student_heights)

# sum_height = 0
# n = 0 # counter variable
#
# for height in student_heights:
#
#   # sum_height = sum_height + height
#   sum_height += height
#   # n = n + 1
#   n += 1
#
# aver = sum_height/n
# print(aver)
###########################################

#Question 01

# You are going to write a program that calculates the sum of all the even numbers from 1 to a user input number. Thus, the first even number would be 2 and the last one is the user input number:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 +...+user input number

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

#Write your code below this row

# num = int(input("Tell me an integer?"))
#
# sum = 0
#
# for i in range(2,num+1,2):
#   print(sum)
#   sum += i




#############################################
