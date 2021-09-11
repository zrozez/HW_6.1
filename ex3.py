from functools import reduce

numbers = [4, 17, 3, 90, 28, 55]

numbers1 = reduce(lambda x,y:(x*y), numbers)*1.5
