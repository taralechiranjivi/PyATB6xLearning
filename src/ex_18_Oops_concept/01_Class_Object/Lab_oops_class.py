class Person:
    # Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    # Behaviour
    def talk(self):  # self - this , self will be first argument in every behaviour.
        print("I can Talk")


    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def method_walk_return(self):  # No Arg with Return
        return "I am walking"




def function_outside():
    print("Outside")

# Create an Object of the Class
# ObjectRef = ClassName() -> Object
geeta = Person()
amit = Person()
navita = Person()
print(geeta.name) # - A
geeta.sleep("pramod") # - B

class Dog:
    #A
    name = None
    breed = None
    height = None
    weight = None


    #B
    def bark(self):
        print("Barking")
        # print(name)
        print(self.name)

    def talk(self):
        print("Talking")

print("Outside ?")
chow  = Dog()
# Dog() - Object
# chow -> Object Ref.

rancho = Dog()