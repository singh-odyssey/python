# find the maximum number in a list using reduce func.

from functools import reduce

l=[1,2,32,43,234,556,5336,453]
largest = reduce(lambda x, y: x if x > y else y, l)
print("The largest number is:", largest)