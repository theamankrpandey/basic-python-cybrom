# class student:
#     def __init__(self,name,quali):
#         self.n=name
#         self.q=quali
# obj1 = student("aman","b.e")
# print(obj1.n)


class car:
    def __init__(self,fullname,brand,model):
        self.fullname=fullname
        self.brand=brand
        self.model=model
    def car1(self):
        return f"{self.brand} {self.fullname}"
s1=car("toyota","korola","xxxcv")
# print(s1.fullname,s1.model,s1.brand)
print(s1.car1())