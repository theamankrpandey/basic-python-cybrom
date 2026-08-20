# hiding the internal funtionality from user
# from abc import ABC,abstractmethod
# class webpage():
#     def dashboard(self):
#         print("welcome to dashboard")
#     def userprofile(self):
#         print("welcome to profile page")
#     # @abstractmethod
#     def login(self,user,password):
#         self.user=user
#         self.password=password
# class user():
#     def login(self,user,password):
#         print("hello")
# # obj=user()
# # obj.dashboard() 
# # obj.userprofile()
# obj1=login("aman",9031443522)
# print(obj1.login)




# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("vehicle is being started in few minutes")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike Start")


# obj = Bike()
# obj.start()
# obj1=Vehicle()
# obj1.start()




a = [1,2,3]
# b= [2,3,4]
# c=[]

# i =0;
# while i <3:
#     c+= [a[i]+b[i]]
#     i+=1
# print(c)


c=a[0]
for i in a:
    if i>c:
        c=i
print(c)