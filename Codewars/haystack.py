""" Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so: """


def findNeedle(needle):
    position = 0
    for i in needle:
         if i == "needle":
            position = needle.index("needle")
    return f"found the needle at position {position}"

print(findNeedle(['3', '123124234', None, 'needle', 'needle', 'needle', 2, '3']))
print(findNeedle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']))
