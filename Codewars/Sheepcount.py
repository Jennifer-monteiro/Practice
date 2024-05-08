def count_sheeps(sheep):
    count_total = 0
    for x in sheep:
        if x == True:
            count_total = count_total + 1 
    return count_total

print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))