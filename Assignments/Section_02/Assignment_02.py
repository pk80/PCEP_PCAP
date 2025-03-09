# Assignment 2
# Using some of the collection data types we learned about
# in the course so such as a list and dictionary, create a
# data structure that best represents the following scenario:
#
# Tom has a salary of 20000 and is 22 years old. He owns a few items such as
# a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
# who owns a bike, a laptop and boat.

# Solution
my_list = {'Tom': {'salary': 2000, 'age': 22, 'items': ['jacket', 'car', 'TV']},
           'Mike': {'salary': 24000, 'age': 27, 'items': ['bike', 'laptop', 'boat']}}

print("Mike's age is : ",my_list['Mike'].get('age'))
print("Mike's items are : ", ', '.join(my_list['Mike'].get('items')))
