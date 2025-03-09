# Assignment 3
# There is a list shown below titled original_list.
#
# Using only what you've learned so far in the course,
# write code to create a new list that contains the tuple sorted.
#
# IMPORTANT: you must do this programmatically! Don't just
#       hard code a new list with the values rearranged.

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

# Solution
tuple_list = [original_list[3][0], original_list[3][1], original_list[3][2]]
tuple_list.sort()
sorted_tuple = (tuple_list[0], tuple_list[1], tuple_list[2])
new_list = original_list[0:3]
new_list.append(sorted_tuple)
print(new_list)
