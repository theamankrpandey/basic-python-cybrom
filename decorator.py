# def outer(x):
#     def inner(p,q):
#         p=p+5
#         q=q+10
#         x(p,q)
#     return inner
# @outer
# def display(x,y):
#     print(x+y)
# display(10,20)

# def hello(x):
#     def hii(p,q,r):
#         p=p+5
#         q=q+10
#         r=r+10
#         z=x(p,q,r)
#         return z
#     return hii
# @hello
# def hyy(a,b,c):
#     return a+b+c
# res=hyy(2,4,6)
# print(res)

    
# def div1(func):
#     def inner(x,y):
#         if x<y:
#             x,y = y,x
#         return func(x,y)
#     return inner
# @div1
# def div(a,b):
#     return a/b
# res=div(2,4)
# print(res)


# def decoratoro(x):
#     def hello():
#         print("teansaction initiated")
#         x()
#         print("transaction succesful")
#     return hello
# @decoratoro
# def hii():
#     print("excuating all steps")
# hii()