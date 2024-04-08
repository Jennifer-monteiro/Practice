"""  Write a function that removes the spaces from the string, then return the resultant string """

def no_space(x):
    new = x.replace(" ","")
    return new

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

def no_space2(y):
    new2 = y.strip()
    return new2

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  BC'))
