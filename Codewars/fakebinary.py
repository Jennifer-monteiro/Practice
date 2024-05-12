""" Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string """

def check(string):
    new_string = []
    for i in string:
        if int(i) < 5:
            new_string.append('0')
        elif int(i) >= 5:
            new_string.append('1')
    
    new_string = ''.join(new_string)
    
    return new_string

print(check('366058562030849490134388085'))