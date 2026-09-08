# class student:
#     '''hhh'''
# print(id(student))
# obj1=student
# print(id(obj1))
# obj2=student
# print(id(obj2))
# print(student.__doc__)


# class student:
#     def show():
#         print("welcome")
# print(student.show())

# class student:
#     pass 
# obj=student()
# obj1=student()
# print(id(student))
# print(id(obj))


# class student :
#     def __init__(self):
#         print("welcome")
# obj=student()

# class student:
#     # grade="10th"
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#     @classmethod
#     def change(cls,newgrade):
#         cls.newgrade=newgrade

# obj1=student("aman",101)
# print(obj1.n,obj1.r)
# obj1.change("12th")
# print(obj1.newgrade)





class GrandParent:
    def house(self):
        print("House")

