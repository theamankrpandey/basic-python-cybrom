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
# class a:
#     _x=10
#     def _show(self):
#         print("hello")
# class b(a):
#     pass
# obj=b()
# print(obj._x)
# obj._show()
# print(a._x) #accessible but as per the documentation it's not accessible



# private variable(method)
class a:
    __x=10
    def __show(self):
        print("hello")
class b(a):
    pass
obj=b()
# try:
#     print(obj.__x)
# except AttributeError:
#     print("hello")
print(obj.__x)
# obj.__show()
# print(a.__x) #accessible but as per the documentation it's not accessible
print(dir(a))
