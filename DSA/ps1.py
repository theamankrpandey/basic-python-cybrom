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


# print a function for fibonacci series
# def fibo(n):
#     ft = 0
#     st = 1
#     print(ft, st, end=" ")     
#     for i in range(2, n):      
#         next = ft + st
#         print(next, end=" ")
#         ft = st
#         st = next

# fibo(6)



# Finding the Second Largest Number in an Array
# Input:
# array = [10, 20, 4, 45, 99]
# Output:
# 45

# def sort(n):
#     l=len(n)
#     for i in range(0,l):
#         for j in range(i+1,l):
#             if n[j] > n[i]:
#                 n[j],n[i]=n[i],n[j]
#     return n
# num=[10, 20, 4, 45, 99]
# p=sort(num)
# print(p[1])


# Input:
# [2 4 6 8 10]
# Output:
# 18
# Explanation:
# Values at even indices: 2 (index 0), 6 (index 2), 10 (index 4). Sum = 2 + 6 + 10 = 18.
# n =[2,4,6,8,10]
# result=0
# for i in range(len(n)):
#     if i % 2 ==0:
#         result+=n[i]
# print(result)