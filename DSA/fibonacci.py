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