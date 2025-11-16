# # SET
# # Collection of Unique
# # {} - parenthesis
#
# list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
# print(list_of_unique_items)
#
# list1 = [45.2, 33, 33, 45, 21]
# set1 = set(list1)
# print(set1)
#
# t = ("TheTestingAcademy", "for", "TheTestingAcademy")
# print(t)
# print(set(t))
#
# mixed = {1, "QA", True, 3.5}
# print(mixed)
#
# empty = set()
# print(type(empty))
#
# for item in mixed:
#     print(item)
#
# mixed.add(10)
# print(mixed)
# mixed.remove(10)
# print(mixed)

mixed = {1, "QA", True, False, 3.5}
print(mixed)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)            # {1, 2, 3, 4, 5}
# print(a.union(b))       # same result
#
#
# print(a & b)            # {3}
# print(a.intersection(b))
#
# print(a-b)
# print(b-a)
#
# print(a ^ b)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)
print(len(set1))

for i in set1:
    print(i)

set1.add("Pramod")
set1.add("Pramod")
print(set1)

squares = {x ** 2 for x in range(5)}
print(squares)

# Frozen Set (Immutable Set)
# A frozenset cannot be changed after creation.
my_list = [1, 2, 3, 3]
fset = frozenset(my_list)
print(fset)
# fset.add(4) #AttributeError: 'frozenset' object has no attribute 'add'