
# Scope - part of the program where an object or name may be accessible


# Global scope - defined in the main body of a script
# Local scope - defined inside a function
# Built-in scope - names in the pre-defined built-ins module

# n=5
# def power(k=1):
#
#     n = 2**k # Local Variable
#     print(n)
#     # return n
#
# power(3)
# print(n)
# ans = power(3)
#
# print(ans)





# Global vs Local scope



# def square(value):
#     new_val=value ** 2
#     return new_val
#
# print(square(3))
#
# print(new_val)


############################################

# new_val=10
#
# def square(value):
#     new_val = value ** 2
#     return new_val
#
# print(square(3))
#
# print(new_val)


############################################

# new_val=20
#
# def square(value):
#     global new_val
#     new_val = new_val ** 2
#     return new_val
#
# print(square(3))
#
# print(new_val)

###################################################
#Nested Functions
# def mul2plus5(x1, x2, x3):
#     new_x1 = x1 * 2 + 5
#     new_x2 = x2 * 2 + 5
#     new_x3 = x3 * 2 + 5
#     return (new_x1, new_x2, new_x3)

####################################################
#
# def mul2plus5(x1, x2, x3):
#
#     def inner(x):
#         return x * 2 + 5
#
#     return (inner(x1),inner(x2), inner(x3))
#
# print(mul2plus5(1,2,3))

###################################################
# def raise_val(n):
#
#     def inner(x):
#         raised = x ** n
#         return raised
#     return inner
#
# square = raise_val(2)
# print(square)
# # cube = raise_val(3)
# # print(square)
# print(square(3))



# def outer():
#
#     n = 1 # Enclosing
#     def inner():
#         nonlocal n #If you want to overwrite a local variable
#         n = 2 # Local
#         print(n)
#     inner()
#     print(n)
#
# outer()

#LEGB rule - local, enclosing, global, built-in (example, print)

# print(v_new)

# When u is a local variable
def add_ten(x):

    y = x + 10

    return y

ans = add_ten(7)

print(ans)


############################################################
y = 20 # Global
def add_ten(x):
    global y
    y = x + y + 10 # Local

    return y

ans = add_ten(7)

print(ans)


#######################################################


def outer(x):

    y = 7 # Enclosing
    def inner(z):
        nonlocal y
        y = y + z # local
