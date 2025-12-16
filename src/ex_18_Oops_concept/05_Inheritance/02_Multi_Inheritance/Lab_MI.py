class APIBase:
    def api_auth(self):
        print("Authenticatin API")


class DBBase:
    def db_connect(self):
        print("Connecting to the DB")


class TestHybrid(APIBase, DBBase):
    def run(self):
        self.api_auth()
        self.db_connect()
        print("Test Case Running.")


tc1 = TestHybrid()
tc1.run()

# Example
class Father1:
    def money(self):
        print("F1 Money")

class Father2:
    def money(self):
        print("F2 Money")

# class Child(Father1, Father2):
class Child(Father2, Father1):
    def give_money(self):
        print("Son")
        self.money()

c = Child()
c.give_money()