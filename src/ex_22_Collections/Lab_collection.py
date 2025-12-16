from collections import *

# # COUNTER - data s
# user_input = input("Enter a string")
# count_char = Counter(user_input)
# print(count_char)

# namedtuple
# info = ('Pramod', 34, True, 9.8)
# print(info)

info = namedtuple('info', ['name', 'age', 'ismarried', 'number'])
t = info('pramod', 34, True, 9.8)

print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)


### main method
def main():
    print("Main called!")

if __name__ == "__main__": # Python int - main ->
    main()


#### MAin Use
def f1():
    print("f1")

def f2():
    print("f2")


def f3():
    print("f3")

def main():
    print("main from 176")

if __name__ == "__main__":
    main()
    f1()
    f2()
    f3()


#
# import os
#
# print(os.getcwd())
# full_path = os.path.join(os.getcwd(),"pramod.txt")
# # full_path = os.path.join("Users\G COMPUTER\PycharmProjects\PyATB6xLearning\src\ex_22_Collections\Lab_collection.py","pramod.txt")
# print(full_path)

# file = open(full_path, 'r')
# print(file.read())


