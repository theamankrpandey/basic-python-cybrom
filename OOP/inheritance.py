# class student:
#     x=10
#     y=20
#     def new (self):
#         print("from new")
# obj=student()
# print(f'x= {obj.x} and y= {obj.y}')

# single level inheritance
class parent:
    car="nexon"
    def home (self):
        print("home from parent")
class child(parent):
    def home (self):
        print("home from child")
        super().home()
obj=child()
# obj.home()
obj.home()