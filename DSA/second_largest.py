
def second_largest(n):
    if len(n)<2:
        return
    largest=float("-inf")
    second=float("-inf")
    for i in n:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    return second
n=list(map(int,input("enter a number with space").split()))
p=second_largest(n)
print(p)