nums = [1, 2, 3, 4, 5, 6]


def even_num(x):
    return x % 2 == 0


print_even_numbers = list(filter(even_num, nums))
print(print_even_numbers)

list_student = [50, 51, 100]


def keep(x):
    if x > 50:
        return True


all_student = list(filter(keep,list_student))
print(all_student)

# example

test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

pass_give = list(filter(lambda x: x == "PASS", test_results))
print(pass_give)

# example
names = ["QA", "", "Automation", "", "Tester"]


def non_empty(x):
    if x != "":
        return True
    return None

non_empty = list(filter(non_empty, names))  # removes empty strings
print(non_empty)

### Map
numbers = [1, 2, 3, 4, 5]


def sq(x):
    return x ** 2


sq_all_numbers = list(map(sq, numbers))
print(sq_all_numbers)

name = ["pramod", "dutta", "qa", "lucky"]


def upper_case(string):
    return string.upper()


upper_names = list(map(upper_case, name))
print(upper_names)

response_times_ms = [1200, 1500, 1800]


def mil_sec(x):
    return x / 1000



# response_times_s = list(map(mil_sec, response_times_ms))
response_times_s = list(map(lambda x: x/1000, response_times_ms))
print(response_times_s)