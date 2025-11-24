l=[2,4,1,3,5,6]
n=len(l)
for i in range(0,n):
    for j in range(i+1,n):
        if l[j]<l[i]:
            l[i],l[j]=l[j],l[i]
print(l)