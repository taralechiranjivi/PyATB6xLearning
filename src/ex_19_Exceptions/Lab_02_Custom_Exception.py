
### Custom_Exception
class InvalidAgeException(Exception):
    pass

def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")

def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")

can_you_drink(17)
can_you_drink(25)


# ### REAL_Selenium_Ex_TESTING
# from selenium.common.exceptions import NoSuchElementException
# from selenium import webdriver
#
# try:
#     driver = webdriver.Chrome()
#     driver.get("https://example.com")
#     driver.find_element("id", "not exist button")
# except NoSuchElementException as nse:
#     print("Element not found!", nse.msg)


### FileNotFoundError
# try:
#     data = open("test.json").read()
# except FileNotFoundError as fnf:
#     print(fnf)


# class A:
#     pass

# class B(A):
#     pass


# eg = ExceptionGroup("Multiple Ex", [
#     ValueError("Invalid Value"),
#     TypeError("Type Error "),
#     ZeroDivisionError("Can't div Xero")
# ])
#
# def check_div(a):
#     if a == 0:
#         raise eg


