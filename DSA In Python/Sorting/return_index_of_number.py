def check(no):
    n=int(input("enter a number"))
    for i in range(0,len(no)):
        if i==n:
            return i
    return -1 
        
nums=[1,2,3,4,5,6]
print(check(nums))