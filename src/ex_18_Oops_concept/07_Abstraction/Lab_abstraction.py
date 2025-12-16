# Abstraction
# Hide the details and show what is required.
# Car - with key _ __private, tyres -> public,
# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog("PP")
dog.sound()

# ===========================
# from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):

    def loan(self):
        print("Giving the 50K loan")

amit = Amit("AMIT SHARMA")
amit.loan()
# ==========================

# Real Automation exaple
# from abc import ABC, abstractmethod

class BrowserManger(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop command, common")


class ChromeBrowser(BrowserManger):

    def start(self):
        # t = ChromeDriver()
        print("We are starting the chrome")

tc = ChromeBrowser()
tc.start()
tc.stop()
# ===================
# Example
# from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod
    def setGear(self):
        pass

class Engine:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine,GearBox):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()

tesla = Car()
tesla.drive()

# =========================
# Exaple
from abc import ABC, abstractmethod


class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()
tc1 = TC1()
tc1.runTc()