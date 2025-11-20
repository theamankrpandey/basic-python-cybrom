# head recursion
# count=0
# def hello():
#     global count
#     if count==4:
#         return
#     print("aman")
#     count+=1
#     hello()
# hello()

# tail recursion or backtracking
# count=0
# def hello():
#     global count
#     if count==4:
#         return
#     count+=1
#     hello()
#     print("aman")
# hello()

# factorial using recursion
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# print 1 to n using recursion tail calling first printing l
# def hello(i,n):
#     if i<n:
#         return
#     hello(i-1,n)
#     print(i)
# hello(10,1)

#use funtional recursion funtional recursion
# def hello(sum,a,b):
#     if a>b:
#         print(sum)
#         return
#     hello(sum+a,a+1,b)
# hello(0,1,3)

# funtional recursion
# def hello(n):
#     if n==1:
#         return 1
#     return n+hello(n-1)
# print(hello(3)) 

# waf to print factorial of a number
# def hello(n):
#     if n==0:
#         return 1
#     return n*hello(n-1)
# print(hello(5))