# def sort(l):
#     n=len(l)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if l[j]<l[i]:
#                 l[j],l[i]=l[i],l[j]
#     return l
# num=list(map(int,input("enter a list").split()))
# print(sort(num))



# v=["a","e","i","o","u"]
# d={}
# for i in v:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


l = list(map(int, input("enter a list: ")))

n = len(l)

for i in range(0, n):
    for j in range(i + 1, n):
        if l[j] < l[i]:
            l[j], l[i] = l[i], l[j]

print(l)