class MathClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b):
        return a + b


obj_ref = MathClass()
obj_ref.add(3,4)
obj_ref.add(3.14,4.14)
# =========================

class Person:
    def say_name(self, name):
        print("Hi", name)

    def say_name(self, name, lastname="Dutta"):
        print("Hi,", name, lastname)

t = Person()
t.say_name("Pramod")
# ==================================
class MathClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=10):
        return a + b + c


obj_ref = MathClass()
obj_ref.add(3, 4, 5)
obj_ref.add(3.14, 4.14)

# ==================
class Browser:

    def make_http_request(self, url):
        print("Hi, Lets make the HTTP request without auth", url)

    def make_http_request(self, url, auth=None):
        print("Hi, Lets make the HTTP request with auth", url, auth)


t = Browser()
t.make_http_request("google.com","admin")