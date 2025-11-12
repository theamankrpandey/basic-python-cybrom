# Write a Python program to create a frequency map of elements in a collection.
# simple method
# n=list(input("enter a collection"))
# a={}
# for i in range(0,len(n)):
#     if n[i] in a:
#         a[n[i]]+=1
#     else:
#         a[n[i]]=1
# print(a)

n=list(input("enter a collection"))
a={}
for i in range(0,len(n)):
    a[n[i]]=a.get(n[i],0)+1
print(a)