from doctest import Example


def add_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards, License")
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")


@add_security
def drvie_zypp_scooter():
    print("Drving Zypp scooter")

# Decorators example
def before_after_ui_test(func):
    def wrapper():
        print("Before Running UI Code")
        func()
        print("After Running UI Code")
    return wrapper()


@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")


# Without Decorators
def start():
    print("Before the running UI TC")
    print("Start the Browser ")

def end():
    print("End the running UI TC")
    print("Quit the Browser ")

def test_ui():
    print("I will Test the UI")


start()
test_ui()
end()

# Real Decorators Example
import time


def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the log")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
    return wrapper

@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@time_decorator
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)

test_ui_1()
test_ui_2()

# Example 2
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator1
@decorator1
def say_hello():
    print("Hello!")


say_hello()

# Interview QUE
# Checking for a Leap Year , 2024 → Yes
#
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# year = 2024
year = 2025
result = check_leap_year(year)
print(result)

# # time Imprt
# import time
# print(time.time())
# print(time.sleep(4))
# print(time.localtime().tm_hour)
# print(time.localtime().tm_min)
#
#
# time.sleep(4) # halt the program for the 4 seconds







