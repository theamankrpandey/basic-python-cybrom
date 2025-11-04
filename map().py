l=1,2,3,4,5
def squar(n):
    print( n*n)
result = map(squar,l)
print(result)
print(list(result))

# l1=[1,3,5,7]
# l2=[1,2,3]
# l3=[1,2,3,4,5,6,7]
# def add (x,y,z):
#     return x+y+z
# result=list(map(add,l1,l2,l3))
# print(result)


# l1=(1,2,3,4)
# l2=(1,2,3,4)
# l3=(2,3,4,5)
# def hello(n):
#     if n%2==0:
#        return "even"
#     else:
#         return "odd"
# result=map(hello,l1)
# print(list(result))