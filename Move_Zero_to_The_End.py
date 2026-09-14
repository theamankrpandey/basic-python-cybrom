a=[0,2,3,0,4,6,9,5,0,7,0]
j=0
for i in range(len(a)):
    if a[i]!=0:
        a[i],a[j]=a[j],a[i]
        j+=1
print(a)
