# 1. Dictionaries
# This type of data structure is a set of key value pairs
# They are not positional oriented but are key oriented
# They are mutable
# They cannot be sorted

my_dict = {'k1': 'some data', 2: [1, 2, 3], 'k2': ('1', '2', '3'), 'k4': True}
print(my_dict)

# type method
print(type(my_dict))

# accessing elements
print(my_dict['k1'])
print(my_dict['k2'])

# change data
my_dict['k4'] = False
print(my_dict)

# no sort method
people_dict = {'john': 134, 'mike': 170, 'robert': 165}
print(people_dict)
# people_dict.sort() # AttributeError: 'dict' object has no attribute 'sort'

# pop method
# must specify key for pop method in dictionaries
# pop returns only the value not the entire key-value pair
result = people_dict.pop('mike')
print(result)
print(people_dict)

# clear method
# dictionary will not be deleted but only elements are deleted
people_dict.clear()
print(people_dict)

# adding new data
my_dict['k3'] = (1, 2, 3)
print(my_dict)

# remove tuple from a dictionary
tuple_removed = my_dict.pop('k3')
print(tuple_removed)

# del keyword to remove item from dictionary
del my_dict[2]
print(my_dict)
