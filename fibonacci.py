def fibo(n):
    f=0
    s=1 # 0 1 1 2 3 5
    print(f,s,end=" ")
    i=0
    next=f+s
    while i<=n:
       next=f+s
       print(next,end=" ")
       f=s
       s=next
       i+=1
n=int(input("enter a number"))
fibo(n)

# n = int(input("enter"))

# a = 0
# b = 1

# for i in range(n):
#     print(a)

    # c = a + b
    # a = b #1
    # b = c #1        


'''Easy Approach'''
n = int(input("Enter a number: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


