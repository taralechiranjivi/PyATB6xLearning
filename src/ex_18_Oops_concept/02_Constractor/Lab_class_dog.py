print("Outside the class")


class MobilePhone:
    model = None

    def __init__(self):
        print("DC")

    def talk(self):
        print("Hi,talking")


iphone = MobilePhone()
iphone.talk()
print("Outside the class2")

class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, nameGiven, breedGiven):
        print("Param C")
        self.name = nameGiven
        self.breed = breedGiven

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleep -> " + self.name)

    def talk(self):
        pass


chow = Dog("chow", "mastiff")
rancho = Dog("rancho", "desi")

chow.sleep()
rancho.sleep()

class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None
    def __init__(self):
        print("I will be called")

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog()
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)

# Dog().talk()

### user Input
class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        print("Let's take the user input, Please share the name,age,phone,occ")
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the Phone\n")
        self.occupation = input("Enter the occupation\n")

    def display_values(self):
        print("Name is ", self.name, "Age is ", self.age, "Phone is", self.phone, "occupation", self.occupation)

amit = Person()
amit.display_values()

### Cal Non Pcclass Calc:
class Calc:
    a = None
    b = None

    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


a = float(input("Enter the value of a"))
b = float(input("Enter the value of b"))

object_ref = Calc()


output_sum = object_ref.sum(a, b)
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_div = object_ref.div(a, b)
print(output_sum, output_sub, output_mul, output_div)


class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b



    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_Ref = Calc(3, 4)
print(object_Ref.sub())
print(object_Ref.sum())
print(object_Ref.div())
print(object_Ref.mul())