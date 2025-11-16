print("Hello World")


name= input("Enter the name")

# Step 1 - Declare / Define
def greet():
    print("Hi")

# Step 2 - Calling
greet()

# Step 1 - Declare / Define
def greet():
    print("Hi")

# Step 2 - Calling
greet()
greet()
greet()
greet()

def greet(name):
    print("Hi,", name)


greet("Pramod")
greet("Amit")
greet(34.56)


def greet_first_last_name(firstname, lastname):
    print("Your full name is, ", firstname, lastname)

greet_first_last_name("Pramod","Dutta")

def FUNCTION_NAME():
    print("Yes")

FUNCTION_NAME()

#Type 3 - with param and returns also.

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 5)
print(result)

def greet_with_default_param(name="QA"):
    print("Hi,", name)


greet_with_default_param("Pramod")
greet_with_default_param("Amit")
greet_with_default_param()

def math_operations(a, b):
    return a + b, a - b, a * b


sum_result, diff_result, mul_result = math_operations(3, 4)
print(sum_result)
print(diff_result)
print(mul_result)

def display_information(name, role):
    print(f"Name : {name}, role is {role}")
    # print("Name: ", name, "role is ", role)


# display_information("Pramod", "QA")
# Better Version
display_information(name="Pramod2", role="QA2")
display_information(role="QA3", name="Pramod3")

# Write a Program , take a user name and say Hello to Him

user_input = input("Enter your name\n")


def say_your_name(name):
    print("Hi,", name)


say_your_name(user_input)

# Function Types
# User Defined
# 1. They can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments

import math

# built in functions
result = max(3, 4)
print(result)


# 1. They can't return -> non return
# No Return Type and No Parameter / Argument - NRNP

def greet():
    print("Hello")


greet()


# 2. # No Return Type and with Argument/ Param
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Pramod")


# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="Pramod"):
    print("Hello", name.upper())


say_hello_default_arg("Dutta")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, name2)


multiple_args()
multiple_args("Lucky", "Sharma")
multiple_args(name1="Pramod")
multiple_args(name1="Dutta", name2="Amit")
multiple_args(name2="Amit")


# def test(name):
#     return name
# test("test")

# 4. Argument + return Type

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 56)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)

# Function Intervview QUE

# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P
# I/O -  int
# O/P - int

# Step 2 - Rough Logic
# return n1+n2+n3


# Step 3 - Write Logic

num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))


def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result = sum_of_three(num1, num2, num3)
result0 = sum_of_three(30, 40, 56)
result1 = sum_of_three()
result2 = sum_of_three(n1=10)
result3 = sum_of_three(n1=10, n2=30)
result4 = sum_of_three(n1=10, n2=30, n3=40)
result5 = sum_of_three(n3=num3)

print(result0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result4)


def sum_of_three_numbers(a, b, c):
    return a + b + c


result1 = sum_of_three_numbers()
result2 = sum_of_three_numbers(30, 40, 50)
result3 = sum_of_three_numbers(a=1, b=2)

# QUE
def sum_three(a=1, b=1, c=1):
    return a + b + c


result1 = sum_three()
print(result1)

result2 = sum_three(1, 2)
print(result2)

result3 = sum_three(1, 2, 3)
print(result3)

result5 = sum_three(b=67, a=10, c=45)
print(result5)

result6 = sum_three(a=10, b=67, c=45)
print(result6)

# Infinte Argument
def print_mul_arg(*pramod_list):
    # args - List
    for i in pramod_list:
        print(i)


print_mul_arg("pramod")
print_mul_arg(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)
print_mul_arg("pramod", "dutta")
print_mul_arg("pramod", "dutta", "third")
print_mul_arg("pramod", "dutta", "third", 3.14)
print_mul_arg("pramod", "dutta", "third", 3.14, True)

# Real Args

# Pizza Lovers
# Toppings - corn, paneer, lives, cheese, pineapple, jalapeno, capsicm

def make_pizza(*toppings):
    print(toppings)

pramod = make_pizza("cheese","corn")
yoga = make_pizza("cheese","corn","paneer","capsicm")
vinay = make_pizza("tomato")

#
# greet_rashmi()
#
# def greet_rashmi():
#     print("Hi,Rashmi")

# Outer And Ineer Def
def f1():
    print("Welcome")
    #Step 1- Declare
    def f2():
        print("Hi")

    #Step 2 - Call
    f2()

f1()
# f2()

# Simple QUE
def validate_status_code(response_code):
    if response_code > 0:
        if response_code == 200:
            print("Request is success")
        else:
            print("Error is the request")
    else:
        print("Error in the response code value.")

validate_status_code(404)
validate_status_code(200)
validate_status_code(response_code=200)
validate_status_code(input("Enter your status code"))

