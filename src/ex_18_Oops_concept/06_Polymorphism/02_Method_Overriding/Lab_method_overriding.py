class BaseTest:
    def run(self):
        print("Running generic test")


class LoginTest(BaseTest):

    def run(self):
        print("Running Login Test")


# t = LoginTest()
t = BaseTest()
t.run()
# =======================

class TestSuite:
    def info(self):
        print("Test suite information")

class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base test execution")

class LoginTest(BaseTest):
    def run(self):  # overriding
        print("Login test execution")

class APITest(BaseTest):
    def run(self):  # overriding
        print("API test execution")

# t = LoginTest()
# t = APITest()
t = BaseTest()
t.run()