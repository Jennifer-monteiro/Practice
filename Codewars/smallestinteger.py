def smallest_int(arr):
    result = sorted(arr)
    return result[0]

print(smallest_int([78, 56, 232, 12, 11, 43])) 

def smallest_int(arr):
    smallest = float('inf')
    for i in arr:
        if i <= smallest:
            smallest = i
    return smallest
print(smallest_int([78, 56, 232, 12, 5, 43]))