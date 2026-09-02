n = int(input("enter a number"))
if n<=1:
    print("not a prime number")
else:
    count =0
    for i in range(2,n+1):
        if n % i ==0:
            count +=1
    if count ==2:
        print("prime Number")
    else:
        print("Not Prime Number")
        