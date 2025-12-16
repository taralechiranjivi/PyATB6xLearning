class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count +=1



t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count)

#Each time an object is created, count increases.
# count is shared across all objects.
# ======================

class Utility:
    @staticmethod
    def greet_course_name(name):
        print("Hi,", name)

Utility.greet_course_name("PyATB")
# ==================
# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class O:
    @staticmethod
    def sum(a, b):
        return a + b

# t = O() - static methods can be accessed direclty.
print(O.sum(4,5))
# =================
class MathOperation:

    def div(self, a, b):
        return a / b

    @staticmethod
    def sum(a, b):
        return a + b
t = MathOperation()
print(t.div(10, 10))
print(MathOperation.sum(10, 10))
# ==================
# RalExaple
class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")
class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

tc1 = TC1()
tc2 = TC1()
tc1.runTC()
tc2.runTC()