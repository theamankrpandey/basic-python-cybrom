# import functools
# l=[1,2,3,4,5,6]
# def add (x,y):
#     return x+y
# result=functools.reduce(add,l)
# print(result)

from functools import reduce
l=[10,20,30,40,50]
def max(x,y):
    if x>y:
        return x
    else:
        return y
result=reduce(max,l)
print(result)

from functools import reduce
# l = [1, 2, 3, 4, 5, 6]
# def add(a, b):
#     return a * b
# result = reduce(add, l)
# print(result)
# 720
