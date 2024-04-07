""" We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100" """

def number_to_string(num):
    new_string = str(num)
    print(type(new_string))
    return new_string
num = 1
print(number_to_string(num))
