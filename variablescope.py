'''here the example of global and local scope'''
# x,y=10,20
# def hello():
#     p,q=10,20
#     print(p,q)
#     print(x,y)
# print(x,y)
# print(p,q)



# x,y=10,20
# def add():
#     x=20
#     print(x,end=",")
# add()
# print(x)


x,y=10,20
def add():
    # NOTE:- FOR CHANGING LOCAL TO GLOBAL THE VARIABLE USE globals()+[varible_name]
    global z
    z=20
    print(x,end=",")
add()
print(z)

x=12
def add():
    x=10
    print(globals()['x'])
add()
