# class a:
#     x=10
#     def show(self):
#         print("hello")
# class b(a):
#     pass
# obj=b()
# print(obj.x)
# obj.show()
# print(a.x)

# protected variable
# class A:
#     _x=10
#     def _show(self):
#         print("hello")
# class B(A):
#     pass 
# a =A()
# a._show()
# print(a._x)



# private variable(method)
# class a:
#     __x=10
#     def __show(self):
#         print("hello")
# class b(a):
#     pass
# obj=b()
# try:
#     print(obj.__x)
# except AttributeError:
#     print("hello")
# print(obj.__x)
# obj.__show()
# print(obj._a__x) #accessible but as per the documentation it's not accessible
# print(dir(a))
# print(obj._a__show)
# print(obj._a__x)
# obj._a__show()



'''protected Variable'''
# class A:
#     def _show(self):
#         return "aman"
# o = A()
# print(o._show())



'''Private Varibale ''' ''' Name Mangling'''
# class A:
#     def __show(self):    
#         return "aman"
# o = A()
# print(o._A__show())  #accessible but as per the documentation it's not accessible



# t = ([1, 2],[0], 3) 
# t[1].append(99)
# print(t)


