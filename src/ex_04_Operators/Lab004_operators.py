# Arthematic

# +, - , * , /
print(2+2)
print(2-2)
print(2/2)
print(2*2)

a, b = 10, 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000

### Unary Operators
age = +65
age2 = -65
print(age)
print(age2)

how_many_lambo_pramod = -1
how_many_lambo_pramod = how_many_lambo_pramod + 1
print(how_many_lambo_pramod)

### Comparision Operator
x, y = 10, 20
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True

a, b = 5, 10
print(a > 0 and b > 0)  # True
print(a > 0 or b < 0)   # True
print(not (a > 0))      # False

print(2 ** 2)  # ** - power
print(2 ** 3)  # ** - power
print(2 ** 4)  # ** - power

print(5//2) # Q (int)
print(5/2) # Div (always give you float)

#  ==  Compare Operator ( True or False )
print(2 == 2)
print(2 == 3)

is_pramod_married = True
print(not is_pramod_married)
print(is_pramod_married)

# Logical Operator -> bool
# > , <  >= <=
x = 10
y = 20
print(x > y)
print(x < y)

print(" --- ")

a = 10
b = 10
print(a == b)
print(a >= b) # 10 > 10 or 10 = 10

### Operator Example
f = False
t = True
print(f or t)
print(f and t)

x = 10
y = 20
result = (x != y)
print(result)

q, r = divmod(5, 2)
print(q)
print(r)


a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Increment (++) / Decrement (--) Operators
# Good news - Doesn't have ++, -- operator

x = 5
x += 1
print(x)

x -= 1  # x= x-1
print(x)

x *= 3  # x= x*1
print(x)

# Ternary Operator:  if-else statement.
x = 10
y = 20

print("x is grater than y" if x > y else "x is less than y")

# if x > y:
#     print("x is grater")
# else:
#     print("y is greater")

### User Input Ternary
user_age = int(input("Enter your age\n"))

# if user_age >= 18:
#     print("Yes You can go to GOA and vote")
# else:
#     print("Not you can't go and can't vote")

print("Yes You can go to GOA and vote" if user_age >= 18 else "Not you can't go and can't vote")

### Memeberhip Operator
result = 'a' in 'apple'
result2 = 'b' in 'apple'
result3 = 'b' not in 'apple'
print(result)
print(result2)
print(result3)

### Identity Operator
x = [1, 2, 3]
z = [1, 2, 3]
print(x is z)


### for use of math
import math

print(math.pi)
print(math.pow(2, 2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))





