

from functools import reduce

nums = [3, 7, 1, 9, 5]
print( reduce(lambda a, b: a + b, nums))