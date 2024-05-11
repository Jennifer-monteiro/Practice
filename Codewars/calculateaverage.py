""" Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0. """

def find_average(lst):
    if lst == []:
        return 0
    total = sum(lst) / len(lst)
    return total

print(find_average([1, 2, 3]))