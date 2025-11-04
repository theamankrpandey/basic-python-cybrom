l=[1,2,3,4,5,6]
def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return None
result=list(filter(evenodd,l))
print(result)
# [2, 4, 6]


