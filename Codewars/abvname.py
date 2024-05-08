"""  Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

 """

def abv(name):
    name = name.split()
    initials = ''
    for word in name:
        initials += word[0] + '.' 
    return initials[0:-1]

print(abv('Jef Mont'))
    
