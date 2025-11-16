my_tuple = (1, 2, 3)
print(my_tuple)
# my_tuple[0] = 12 # TypeError: 'tuple' object does not support item assignment

# With Mixed Data Types:
info = ("Pramod", 34, True, 9.8)
print(info)

#Tuple with One Element
single=  (3,)
print(type(single)) # <class 'tuple'>

shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real of Tuples
my_tuple = ("tta.com", "sdet.live")
print(my_tuple)
my_api_list = list(my_tuple)

my_api_list.append("item2")

my_api_list2 = tuple(my_api_list)
print(my_api_list2)


# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])


t = tuple()
print(t)

l = list()
print(l)


# Conversion List to Tuple
t1 = tuple(["pramod", "amit", "manisha"])
print(t1)



hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(len(cities))
print("Paris" in cities)
print("New Delhi" in cities)

t = (12, 34, 56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)

colors = ("red", "green", "blue")
for c in colors:
    print(c)

numbers = "Pramod" * 3
print(numbers)
numbers = (1, 2) * 3
print(numbers)

print(" ---------")

nums = (1, 2, 2, 3, 2)
print(len(nums))
print(nums.count(2))
print(nums.index(3))


my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)    # (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)   # [1, 2, 3]
print(max(back_to_list))   # [1, 2, 3]

my_list = [1, 2, 3]
print(my_list[0:2])
print(my_list[-1])