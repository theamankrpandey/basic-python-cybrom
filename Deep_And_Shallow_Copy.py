import copy

'''Shallow copy'''
a = [[10]]
b=copy.copy(a)
print(b)
b[0].append(20)
print(b)
print(a)

'''Deepcopy copy'''
c=copy.deepcopy(a)
c[0].append(12)
print(c)
print(a)