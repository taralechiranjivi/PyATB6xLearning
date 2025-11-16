# print()
# class
# None
# break

import keyword
print(keyword.kwlist)

age = 65
age  = "Akshay"

# Dynamic Typed Language. - It can understand you are doing, want.
pi = 3.14
name = "Akshay"
name = "Tarale"
name = "Ak"
name = "Aaaaaa"
name = "Pata nahi"
name = "CHI"
print(name)

age = 65
_age = 65
print(age)
print(_age)

_ = 12
print(_)
_ = _+1
print(_)

# 123abc = 90   ### syntax Error: Invalid decimal literal
abc123 = "abc123"
print(abc123)

#123abc = 90
_pramod = "amit"
_abc = 23
pi = 3.14
name = "Pramod"
isMale = True

# Type
print(type(_pramod)) # <class 'str'>
print(type(pi)) # <class 'float'>
print(type(isMale)) #<class 'bool'>

complex_number = 2+3j
print(complex_number)
print(complex_number.real)
print(complex_number.imag)
print(type(complex_number))

# Dynamically typed

age = 98
print(type(age))
age = "Pramod"
print(type(age))
age = True
print(type(age))

long_var_name_is_created_here = "Hello"
print(long_var_name_is_created_here)

a = 10
b = 10
c = a + b
print(c)
c = c - 10
print(c)

a = 10 + 34 * 3 - 1
print(a)

# BODMAS
#
# BODMAS is an acronym that helps remember the order of operations in mathematics:
# B: Brackets
# O: Order of powers or roots
# D: Division
# M: Multiplication
# A: Addition
# S: Subtraction

a, b, c = 45, 5.4, "pramod"
print(a)
print(b)
print(c)

print(a, b, c,sep=" | ")

print("Amit", "Teja", "Tushar")

# To find the max - function - prebuilt functions
# Max number between 3,4
# result = max(3,4)
result = max(3,4,5,100,101)
# max(*args) -.unlimited
print(result)

result_min = min(3, 4)
print(result_min)

result = max(3, 4, 67, -1, 190, 999, 100000, 9899, -1)
print(result)

# print("Hello" + 15)    #--- It give an Type Error (can only concentenate str(not "int") to str)
# Python - Concentation No Concept

# If you want to print you need to convert all of the variables in str
print("Hello" + str(15))





