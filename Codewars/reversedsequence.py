""" Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1] """

def sequence(arr):
    new_arr =[]
    for i in range(arr, 0, -1):
        new_arr.append(i)
    return new_arr


print(sequence(5))