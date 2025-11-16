# List - Collection  of items
# grocery List - butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56

my_list = [1, 2, 3]  # Same type of data (int)
my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(type(my_list)) # <class 'list'> , []
print(len(my_list))
print(my_list[0])
print(my_list[2])
# print(my_list[6]) # IndexError: list index out of range


my_list = [1, 2, 3]
my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[1] = "Dutta"

for element in my_list:
    print(element)

# range() this also return the list
for i in range(1, 5):  # 1,2,3,4
    print(i)


my_list = [1, 2, 3]
# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

# extend() - Append a new list
my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()
my_list.insert(1,"Dutta")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)

my_list[1] = "Amit"
print(my_list)

my_list.remove("Amit")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Dutta")

print(my_list)
print(my_copy_list)

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares.pop())  # Remove and return item at index (default last).
print(squares)
print(squares.pop(1))
print(squares)

squares.clear()
print(squares)

# index(element, start, end)
# Returns the index of the first occurrence of the element.
numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))

print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# reverse() Reverses the list in place.

numbers.reverse()
print(numbers)

# max() / min() / sum() Works for numerical lists.
print(max(numbers))  # 40
print(min(numbers))  # 10
print(sum(numbers))  # 120

# Slicing
print(numbers)  # [10, 20, 20, 30, 40]
print(numbers[1:4])  # from index of 1 to 3
print(numbers[-1])  # # Last element

print("apple" in numbers)
print(20 in numbers)

# List Creation and Comprehension
# range(1,5) -> list
l = list(range(1, 5))
print(l)

# Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

# del statement - Deletes an element by index or the whole list.
del numbers[0]
print(numbers)