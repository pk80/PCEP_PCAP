# Lists
# A list data type is a collection (data structure contain multiple values)
# A list is a mutable object (change contents of the list)
# As list is mutable, no need to modify or reassign back to list when any operation is performed
# None is reserved word in python is specific data type resulting nothing

my_list = [1, 2, 3, 4, 5]
print(my_list)

# type of variable
print(type(my_list))

# pop an item from list
# by default pops out last one in the list
# returns the popped value
result = my_list.pop()
print(my_list, 'removed :', result)

# pop an item at specific index
result = my_list.pop(0)
print(my_list, 'removed :', result)

# change / modify list
my_list[0] = 'S'
print(my_list)

# list can also contain list/set/tuple
my_list[2] = ['hello', 'world']
print(my_list)

# append method adds new element at the end of the list
# append also takes iterable as parameter but this modifies original list
my_list.append((1, 2, 3))
print(my_list)
app_list = ['one', 'two']
my_list.append(app_list)
print(my_list, 'original list appended to another list')

# insert method inserts new element at the given index
my_list.insert(0, {'one': 1, 'two': [1, 2]})
print(my_list)

# sort method sorts the elements in ascending or descending
# this method by default sorts in ascending
# this method modifies the object and doesn't return anything
# note: elements should be of same data type for this to be executed
# my_list.sort()
# print(my_list)  # TypeError: '<' not supported between instances of 'str' and 'dict'
my_list = [3, 6, 4, 2, 1, 5]
print(my_list)
my_list.sort()
print(my_list)

# reverse method sorts elements in descending
my_list.reverse()
print(my_list)

# strings are also sorted
my_list = ['3', '6', '4', '2', '1', '5']
my_list.sort()
print(my_list)

# slicing lists
# prints from index 2 to 4
# end index not inclusive
print(my_list[2:4])
# negative indexing
print(my_list[-2:], 'negative indexing')

# len method returns the number of elements in the list
print(len(my_list))

# merging two lists
another_list = [1, 2, 3, 4, 5]
new_list = my_list + another_list
print(new_list)

# ASSIGNMENT
# create another list contains specific contents :
#   - last 3 elements first list combined with last 3 elements of second list
#   - lists are to be sorted and reversed first before concatenating
# this can also be done by defining a new function
first_list = ['b', 'd', 'a', 'z', 'x']
second_list = [4, 5, 3, 1, 2]
# sorting in ascending
first_list.sort()
second_list.sort()
# sorting in descending
first_list.reverse()
second_list.reverse()
# combining last 3 elements
third_list = first_list[-3:] + second_list[-3:]
print('Assignment : {0}'.format(third_list))

# Accessing elements in nested lists
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'banana', 'orange'], 'd']
print(my_list[6])
print(my_list[6][1])

# ASSIGNMENT
# note: multiple nested lists in a list is a bad design
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'banana', ['john', 'robert']], 'd']
print(my_list)
# extract robert from this nested list
print(my_list[6][2][1])
# try to modify second item in the list to 'computer'
my_list[1] ='computer'
print(my_list)
# change robert to doe
my_list[6][2][1] = 'doe'
print(my_list)

