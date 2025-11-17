# class student:
#     x=10
#     y=20
#     def new (self):
#         print("from new")
# obj=student()
# print(f'x= {obj.x} and y= {obj.y}')

# single level inheritance
# class parent:
#     car="nexon"
#     def home (self):
#         print("home from parent")
# class child(parent):
#     def home (self):
#         print("home from child")
#         super().home()
# obj=child()
# obj.home()
# obj.home()

# class atm:
#     def __init__(self):
#         self.pin=""
#         self.balance=0
#         self.menu()
#     def menu(self):
#         user_input=int(input("""How Can I Helf You" 
#         press 1. to create pin
#         press 2. to change pin
#         press 3 to withdraw money 
#         press 4 to exit. """ ))
#         if user_input==1:
#             self.create_pin()
#         if user_input==2:
#             pass
#         if user_input==3:
#             pass
#         if user_input==4:
#             pass
#     def create_pin(self):
#             user_pin=int(input("enter your pin"))
#             self.pin = user_pin
#             user_balance=int(input("enter your balance"))
#             self.balance=user_balance

#             print("pin created succesfully")
# n=atm() 

class student:
    gread ='10th'
    def __init__(self,name,roll):
        self.n,self.r = name,roll
    
    def new(cls,newgrade):
        cls.gread=newgrade
        print(id(cls))
        print(id(student))
# obj=student("aman",19)
# print(obj.n,obj.r) 
obj2=student("ujjwal",102)
obj2.new("12th")
print(obj2.gread)
print(obj2.n)
print(id(student))