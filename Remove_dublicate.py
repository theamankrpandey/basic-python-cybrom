# a= "helllo"
# b =""
# for i in a:
#     if i not in b:
#         b+=i
#     else:
#         pass
# print(b)


'''List'''
a = [1, 2, 1, 2, 3]
b = []
for i in a:
    if i not in b:
        b = b+[i]
print(b)