
### NameError

# a
#print(a)
# # NameError: name 'a' is not defined

### ZeroDivisionError
# print(10/0) #ZeroDivisionError: division by zero

### TypeError
#print( 1 + "1")
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

### ValueError
# print(int("a"))
#ValueError: invalid literal for int() with base 10: 'a'


### IndexError
# my_list = [1, 2, 3]
#print(my_list[4])
# IndexError: list index out of range

### SyntaxError
#while True print("Hello World!")
#SyntaxError: invalid syntax


# a = int(input("Enter num 1"))
# b = int(input("Enter num 2"))
# c = a/b
# print(c)


### Program_Fix_Try_Except
a = int(input("Enter num 1"))
b = int(input("Enter num 2"))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error becoz of the zero div b !=0")


# try:
#     a = int(input("Enter num 1"))
#     b = int(input("Enter num 2"))
#     c = a / b
#     print(c)
# except (TypeError, NameError, ValueError, ZeroDivisionError):
#     print("Error Due to the Type,Name, Value or Zero Div!")


# try:
#     a = int(input("Enter num 1"))
#     b = int(input("Enter num 2"))
#     c = a / b
#     print(c)
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Div Error")



# try:
#     a = int(input("Enter num 1"))
#     b = int(input("Enter num 2"))
#     c = a / b
#     print(c)
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Div Error")
# finally:
#     print("I will always execute!")


### REAL_API_TESTING
# import requests
#
# try:
#     url = input("Enter the url")
#     # response = requests.get("https://google.com")
#     response = requests.get(url, timeout=3)
#     print(response.status_code)
# except requests.exceptions.ConnectionError:
#     print("Error due to the wrong URL or connectioned failed!")
# except requests.exceptions.Timeout:
#     print("Timeout error, not able to laod the URL.")
# except Exception as e:
#     print(e)

### Try_Except_Else_Finally
# try:
#     a = int(input("Enter num 1"))
#     b = int(input("Enter num 2"))
#     c = a / b
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Div Error")
# else: # Runs only if try block succeeds.
#     print(c)
# finally:
#     print("I will always execute!")

### vwo login
def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized Access!!")
    return "Welcome Admin"

# print(vwo_login("pramod"))
print(vwo_login("admin"))

