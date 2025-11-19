class parent:
    def hello(self,name):
        self.n=name
class parent1(parent):
    print("this is parent1 class")
class parent2(parent):
    print("hello this is class parent2")
class child(parent1,parent2):
    def hii(self,name):
        self.n=name
    print("this is child class")
   
obj=child()
obj.hii("aman")
print(obj.n)
obj1=parent()
obj1.hello("aditya")
print(obj1.n)