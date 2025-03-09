# Assignment 1:
"""
    We would like to get the remainder of 15 divided by 4.
    The calculation below does not seem to give us this result.
    How would you change the code to meet the requirement?

    remainder = 15 - 4
    print(remainder

"""

# simple :
remainder = 15 % 4
print(remainder)


# dynamic :
def get_remainder(num1, num2):
    print(num1 % num2)


get_remainder(15, 4)
