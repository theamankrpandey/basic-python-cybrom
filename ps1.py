# x=eval(input("enter any value"))
# if isinstance(x,object):
#     print("user gives integar value")
#     print(type(x))



# n=int(input("enter a number"))
# if n>0:
#     print(f'given value is {n} is positive')
# elif n==0:
#     print(f' gaiven value {n} is  zero')
# elif n<0:
#     print(f'given value {n} is negative')


# n=int(input("enter a number"))
# if n>0 and n<=10:
#     print(f'given value {n} lies in b/w 0-10')
# elif n>10 and n<=20:
#     print(f'given value {n} lies in b/w 11-20')
# elif n>20 and n<=30:
#     print(f'given value {n} lies in b/w 21-30')
# else:
#     print(f' given value {n} not valid for check condition')


# wap print 1,2,3,4,5
# n=int(input("enter a number"))
# i=1
# while (i<=n):
#     if i<=(n-1):
#         print(i,end=",")
#     else:
#         print(i)
#     i+=1



# wap to print sum of numbers
# n=int(input("enter a number"))
# i,sum=1,0
# while (i<=n):
#     sum=sum+i
#     if i<=(n-1):
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i+=1
# print(sum)


# wap to print multiplication of any numbers
# n=int(input("enter a number"))
# i,multi=n,1
# while (i>=1):
#     multi=multi*i
#     if i>1:
#         print(i,end="*")
#     else:
#         print(i,end="=")
#     i-=1
# print(multi)


# num=int(input("enter a number"))
# i=num
# fact=1
# while i>=1:
#     fact=fact*i
#     if i>1:
#         print(i,end="*")
#     else:
#         print(i,end="=")    
#     i-=1
# print(fact)



# armstrong number
# n=int(input("enter a number"))
# count=0
# arm=0
# d=n
# while n>0:
#     count+=1
#     n=n//10
# x=d
# while x>0:
#     digit=x%10
#     arm=arm+digit**count
#     x=x//10
# if(arm==d):
#     print("arm")
# else:
#     print("not")