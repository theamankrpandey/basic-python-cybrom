a=[90,45,67,88,100,3]
smallest = a[0]
largest = a[0]
for i in range(0,len(a)):
        if a[i] > largest:
            largest = a[i]
        if a[i] <smallest:
            smallest = a[i]
print(largest)