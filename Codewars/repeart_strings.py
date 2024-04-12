""" Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times. """

def repeat_str(repeat, string):
    new_string = string * repeat
    return new_string

print(repeat_str(4, "a"))
