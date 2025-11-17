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

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))