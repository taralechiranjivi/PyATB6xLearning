# Write c program to take a user age and
# Let him know if he can go to the CLUB or not
# age is 21

# Logic Building Formula
# step1
# i/p --> age, int
# o/p --> string(result --> Can go to club or not

# step2  Rough Logic (brute force)
"""
age > 21 --> print can go
age < 21 --> print can't go
"""
# step3 write the logic
### if condition
age = int(input("Enter age\n"))
if age >= 21:
    print("Yes, You Can go to CLUB")
else:
    print("No, You Can not go to CLUB")

# step4  check for the edge cases.
# we should consider edge cases such as:
# Negative ages or extremely high value --> program will break.
# Non-numeric input --- ABC
# age which is valid < 130

# step5    optimize the code
# Handle all the edges
### if condition Optimized
age = int(input("Enter age\n").strip())
if age >= 21:
    print("Yes, You Can go to CLUB")
if age <=0 or age >130:
    print("Enter the valid age")
else:
    if age >= 21:
        print("Yes, You Can go to CLUB")
    else:
        print("No, You Can not go to CLUB")

### else if condition
# Find the positive number is even or odd
num = int(input("Enter numbe: ").strip())
if num >= 0:
    if num % 2 == 0:
        print("EVEN")
    else:
        print("Negative value")

### You can write short one-liner conditions using ternary operator
if num > 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative value")


### Problem Find the value max between two.
# Logic Building Formula
# step 1 --> user i\p -->two integers
# step 2 --> o/p --> int 1 which is greater max number it will return.
# 31.4   or 45.34-- float

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1 > num2:
    print("max", num1)
else:
    print("max", num2)
# num1 == num2  -->  Handled

### Problem Find the value max between 3.
# Logic Building Formula
# step 1 --> user i\p -->two integers
# step 2 --> o/p --> int 1 which is greater max number it will return.


num1 = int(input("Enter a num1\n"))
num2 = int(input("Enter another num2\n"))
num3 = int(input("Enter a num3\n"))
### 5 > and 5 > 2-> 5
### num1 > num2 and num1 > num3 --> num1
### num2 > num1 and num2 > num3 --> num2
### num3 --> num3

if num1 >= num2 and num1 >= num3:
    print("max", num1)
elif num2 >= num1 and num2 >= num3:
    print("max", num2)
else:
    print("max", num3)


### Problem Grade Calculator:
### write a program that calculate and display the latter grade
### for a given numerical score(e.g. A,B,C,D,F)
### based on the following grading scale
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# 1 --> user i\p -- score --> int
# 2 --> o\p --> str --> A,B

score = int(input("Enter score: ").strip())
if score > 100 or score <=-1:
    print("congo, You are Superman !!!, you cant get grade!!!")
else:
    if score >= 90 and score <= 100:
        print("Your grade id A")
    elif score >= 80 and score <= 89:
        print("Your grade id B")
    elif score >= 70 and score <= 79:
        print("Your grade id C")
    elif score >= 60 and score <= 69:
        print("Your grade id D")
    else:
        print("Your grade id F")
### float, abc--> try catch (for complete solution this added in code )

















