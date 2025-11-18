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