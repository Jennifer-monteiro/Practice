""" Write a function argumentsLength that returns the count of arguments passed to it. """


def argumentsLength(*args):
    return len(args)

print(argumentsLength(1, 2, 3))