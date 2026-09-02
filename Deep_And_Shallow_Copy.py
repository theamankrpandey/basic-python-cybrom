import copy
a = [[10]]
b=copy.copy(a)
print(b)
b.append(20)
print(b)
print(a)