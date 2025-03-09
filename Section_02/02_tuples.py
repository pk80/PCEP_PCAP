# 1. Tuples
# They are immutable data structures, meaning contents cannot be modified
# They are more or less similar to lists

my_tuple = (1, 2, 3, 'hello', ['one', 'two'], 1)
print(my_tuple)

# type method
print(type(my_tuple))

# access elements by indexing in a tuple
print(my_tuple[4])

# change data in a tuple
# my_tuple[3] = 'world' # Warning: Tuples don't support item assignment
my_tuple[4][1] = '2'  # but cannot modify entire list
print(my_tuple)

# count method
print(my_tuple.count(1))

# slicing tuple
# returns a tuple
result = my_tuple[2:5]
print(result, type(result))
# extracting 4th element which is a list
list_result = my_tuple[4]
print(list_result, type(list_result))
