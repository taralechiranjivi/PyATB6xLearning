class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

mg_hector = Car("Hector","1.5+ Turbo","2024")
mg_hector.start_engine()

# example LoginPage
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Allowed to Login")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

# # example ENV
# from dotenv import load_dotenv
# import os
# class VWOLoginPage:
#
#     def __init__(self, email_arg, password_arg):
#
#         self.email = email_arg
#         self.password = password_arg
#
#     def login_confirm(self):
#         load_dotenv()
#         if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
#             print("Allowed, Login Sucess")
#         else:
#             print("Login Failed")
#
# email = input("Enter the vwo login email ")
# password = input("Enter the vwo login password ")
#
# vwo_object_ref = VWOLoginPage(email,password)
# vwo_object_ref.login_confirm()
#
# print(os.name)
# -------------------------------------------
# Example
# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")
# email = # Read from test data - Excel,CSV or Env file
# password = #Read from test data -Excel.CSV or Env file

# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()
# ------------------------------------------
# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.
class Car:
    def __init__(self):
        self.public_pramod = "pramod"
        self.__private_baby = "pass123"

    def nany(self):
        self.__password_yogesh_private = "345"

object_ref = Car()

print(object_ref.public_pramod)
# print(object_ref.__private_baby)

object_ref.nany()
# -------------------------------------------------
# Example of Bank
class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance  # public
        self.__account_number = account_number  # Private

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

icici = Bank(9876543210, 100)
icici.deposit(100)
icici.check_balance()
# print(icici.__account_number)
# if you are cashier you can see the a/c becoz of the ecapsulation.
icici.show_me_account_number(True)

# ======================================================
class Home:
    def __init__(self):
        self.public_var = "father"
        self._protected_var = "brother"
        self.__private__var_dadsa__dasda__ = "baby"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Private Wife")

object_ref = Home()
# object_ref.__wife()
# object_ref.__private_var

object_ref.mom()
# print(object_ref._protected_var)
# ⚠️ Technically accessible, but not recommended

# =====================================================
class TestExample:
    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api__key = "ABC12345"
    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    def __private_method1(self):
        pass

    def __private_method2(self):
        pass

    def work(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()
obj.work()

# Access levels:
# print(obj.driver)          # ✅ Public — accessible
# print(obj._config)         # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ Private — AttributeError

