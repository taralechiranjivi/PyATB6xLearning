my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "exp": 3

}

print(my_dict)
print(my_dict["age"])
print(my_dict["role"])

my_dict["role"] = "Manual Tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(key, value)

print("age" in my_dict)
print("role" in my_dict)

student_infor = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": "KA"
}

print(student_infor)
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 100
print(student_infor)


## Dict Mul
student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_list = [student_infor1,student_infor2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["address"]["office_address"])

student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "Murthy",
    # "age": 65,
    "age": 120,
    "address": {
        "home_address": "PODI",
        "office_address": "vizag"
    }
}

student_list = [student_infor1,student_infor2,student_infor3]
print(student_list)
print(student_list[2]["address"]["office_address"])

## Dict concepts
keys = ["name", "role", "experience", "abc"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values))
print(my_dict)

# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))

### Dict Frequency Char.
# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.
string = "automation"
string = input("\nEnter the input e.g automation\n")

# {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}
# Logic building
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}

char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

### Missing Key
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.keys())
print(dict1.values())
dict2 = {"a": 1, "b": 2}
missing_keys = set(dict1.keys() - dict2.keys())
print(missing_keys)

### Dict IQ find max Value
# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}

# def min_value_dict(dictionary):
def max_value_dict(dictionary):
    # return min(dictionary.values())
    return max(dictionary.values())

def max_key_dict(dictionary):
    # return min(dictionary.values())
    return max(dictionary.keys())


# print(min_value_dict({"a": 10, "b": 20, "c": 30}))
print(max_value_dict({"a": 10, "b": 20, "c": 30}))
print(max_key_dict({"a": 10, "b": 20, "c": 30}))

### Remove duplicate value
#  Remove duplicate values from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# Output: {'a': 1, 'b': 2, 'd': 3}

unique_value = set()
result = {}

for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result)

### Dict IQ
# p = {"name": "Pramod", "name": "Amit"}
# print(p)
# my_list = [1, 2, 2, 3, 4, 4, 5]


#Check If Two Dictionaries Are Equal
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)

### Dict IQ for Count vowels
input_string = "hello, world!"
# a,e, i,o,u.
# vowel ?
vowels = "aeiou"

vowels_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)
print(vowels_count)
print(result)


