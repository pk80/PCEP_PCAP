# Assignment 1
# Print Bill's salary from the my_list object shown below.
# my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

# Solution
print(my_list[0].get('Bill'))
print(f"Bill's salary is {my_list[0]['Bill']}")
