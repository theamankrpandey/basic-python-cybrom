a =[7,3,4,8,9,1]
i=0
while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            i=0
        else:
            i+=1
print(a)