# Method OverLoading
class ad:
    def add(self,*args):
        return sum(args)

    # def add(self,a,b):
    #     return a+b
obj = ad()
print(obj.add(1,2,2))


"""Method Overriding"""
class Animal:
    def sound(self):
        return "Animal makes sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


print(Dog().sound())
print(Cat().sound())