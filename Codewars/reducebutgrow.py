""" Given a non-empty array of integers, return the result of multiplying the values together in order. Example: """

def grow(arr):
    new_arr = 1
    for i in arr:
        new_arr = new_arr * i
    return new_arr

print(grow([4, 1, 1, 1, 4]))