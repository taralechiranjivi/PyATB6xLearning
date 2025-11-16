# Example
def triple_number(num):
    return num * 3


result = triple_number(3)
print(result)


# Example
#lambda
result_l_f = lambda num:num * 3
print(result_l_f(3))

def add(n):
    return n + 10


l_add = lambda n: n + 10
print(l_add(30))

def mul(a, b):
    return a * b

# Example
mul_l = lambda a, b: a * b
print(mul_l(3, 4))

def sum_three_num(a, b, c):
    return a + b + c


op_f = lambda a, b, c: a + b + c
print(op_f(3, 4, 5))

# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


user_input = int(input("Enter the number"))

check_even_odd_f = lambda num: "Even" if num % 2 == 0 else "Odd"
result = check_even_odd_f(user_input)
print(result)


# example
import math

# def give_me_power(num):
#     return math.pow(num, 2)
#
# op=  give_me_power(10)
# print(op)

# num = int(input("Enter the number"))
# op2 = lambda num: math.pow(num, 2)
# print(op2(num))


op2 = lambda: math.pow(int(input("Enter the number")), 2)
print(op2())