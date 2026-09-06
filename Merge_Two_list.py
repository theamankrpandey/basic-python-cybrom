# a=[1,2,3]
# b=[4,8,6]
# c=[]
# for i in range(len(a)):
#     c+=[a[i]]
# c+=b
# print(c)


'''Without Using Third List '''
a=[1,2,3]
b=[4,8,6]
for i in range(len(a)):
    a+=[b[i]]
print(a)

