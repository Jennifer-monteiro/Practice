""" you will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not. """

def check(arr, value):
    for i in arr:
        if str(i) == str(value):
            return True
    return False
    
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
print(check([101, 45, 75, 105, 99, 107], 107))