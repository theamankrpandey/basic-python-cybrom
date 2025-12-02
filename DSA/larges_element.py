# find largest element in array

a=[2,4,5,6,7,8,101,11]
result=a[0]
n=len(a)
for i in a:
    if i>result:
        result=i
print(f'the Largest element is :- {result}')