age = 65
age +1
print(age)

"""
This is Multiple Line Command
Here the code you write will not Executed
why this is used???
"""
age = 65
print(type(age))

gst = 18.45
print(type(gst))

result_max = max(45, 65)
result_min = min(45, 65)
print(result_max)
print(result_min)

# built In -- Function
# Pre defind given by the pyathon guys to you to use it.

# max()
# min()
# print()
print(pow(2,3))
b = abs(-10)     # Return the absolute value of the argument.
print(b)

# How to take the user input
name = input("Enter your name : ")
# Read a string from standad input
print("Your name is", name)
print(type(name))


# Logic Building
# Step 1
    # I/P --> num1, num2--> iht
    # O/P --> sum, mul, div (Always ask from interviewer), float
# Step 2 --> Rought Logic

num1 = float(input("Enter the number : "))
num2 = float(input("Enter the number : "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

value= input("Enter the value : ")
print(value)
print(type(value))

# String
name = "Akshay"
# Banch of char
c= 'C'    # <class 'str'>
c1= 'C'    # <class 'str'>
print(type(c))
print(type(c1))

print(len(name))
print(name.upper())   # AKSHAY
print(name.lower())   # akshay


age = "70"
print(type(age))

age = 90
print(type(age))

# str() , int(), float(), bool()
# str age --> int
age = int(age)
print(type(age))

name = "This is a big Line"
print(type(name))
name = name + str(1)
print(type(name))

first_name = "Akshay"
last_name = "Tarale"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))


# Escape Sequence
# \n --> new line
# \t --> tab
# \b --> backspace (1 char bachspace)
print("Hello\nWorld")
print("Hello\bWorld")
print("Hello\bWorld")

c = 'C'
c1 = "C"
print(c)
print(c1)

# dir = 'C:\akshay\n.txt'
dir = r"C:\akshay\n.txt"    # raw--> it will print as it is (ignore the escape seq.)
print(dir)

file_path = r"C:\akshay\n.txt"









