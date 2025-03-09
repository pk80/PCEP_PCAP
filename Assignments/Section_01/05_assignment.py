# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string

    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>

"""

chars = "<<[]]]"  # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]


# Your code below:

# simple :
middle_chars_len = int(len(chars) / 2)
print(chars[:middle_chars_len] + word + chars[middle_chars_len:])


# dynamic :
def show_in_middle(chars, word):
    if len(chars) % 2 != 0:
        print('Chars length is not even. Try again')
        return
    middle = int(len(chars) / 2)
    print(chars[:middle] + word + chars[middle:])


show_in_middle(chars, word)
