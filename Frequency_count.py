a=[1,2,3,9,4,9,10,17,10]
s={}
for i in range(len(a)):
    if a[i] not in s:
        s[a[i]]=1
    else:
        s[a[i]]+=1

# '''Second Method '''
# a = [1, 2, 3, 4, 4]

# s = {}

# for i in a:

#     if i not in s:
#         s[i] = 1
#     else:
#         s[i] += 1

# print(s)