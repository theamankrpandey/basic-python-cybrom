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

# n=list(input("enter a collection"))
# a={}
# for i in range(0,len(n)):
#     a[n[i]]=a.get(n[i],0)+1
# print(a)


'''String Frequency count'''
# a="hello"
# b={}
# max=0
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)




'''Max Frequency count '''
a = "hello"

b ={}
max=0
maxchar = ""
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
    if b[i]>max:
        max=b[i]
        maxchar = i
    
print(maxchar,b)