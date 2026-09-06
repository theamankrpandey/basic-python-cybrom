a=[1,2,3,4,4]
s={}
for i in range(len(a)):
    if a[i] not in s:
        s[a[i]]=1
    else:
        s[a[i]]+=1
print(s)