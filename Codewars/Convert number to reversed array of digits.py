""" Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0] """


def digitize(n):
    n = str(n)
    
    reversed_string = n[::-1]
    result = []
    for x in reversed_string:
        result.append(int(x))
       

    return result

print(digitize(12345))
