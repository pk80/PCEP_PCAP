# 1. Comparison Operators
# all comparison / logical expressions return bool type

#  == : equal to
print(10 == 9)  # false
print(10 == '10')  # false
print(10 == 10.00)  # true
print('hello' == 'hello')  # true
print('hello' == 'Hello')  # false

#  != : not equal to
print(10 != 9)  # true
print(10 != '10')  # true
print(10 != 10.00)  # false
print('hello' != 'hello')  # false
print('hello' != 'Hello')  # true

#  >  : greater than
print(10 > 9)  # true
# print(10 > '10')  # TypeError: '>' not supported between instances of 'int' and 'str'
print(10 > 10.00)  # false
print('hello' > 'hello')  # false
print('hello' > 'Hello')  # true

#  >= : greater than or equal to
print(10 >= 9)  # true
# print(10 >= '10')  # TypeError: '>' not supported between instances of 'int' and 'str'
print(10 >= 10.00)  # false
print('hello' >= 'hello')  # false
print('hello' >= 'Hello')  # true

#  <  : lesser than
#  <= : lesser than or equal to


# 2. Logical Operators
# or : f|f-f, f|t-t, t|f-t, t|t-t
print((('hello' == 'Hello') or (10 == 10)))  # true

# and : f&f-f, f&t-f, t&f-f, t&t-t
print((('hello' == 'Hello') or (10 == 10)) and True)  # true

# not
print(not False)
print(not True)
print(not (10 == '10'))
