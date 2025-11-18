class a:
    def home(self):
        print("home from parent")
    def car(self):
        print("home from parent1")
class b:
    def home(self):
        print("home from parent2")
    def bank(self):
        print("home from parent2")
class c(a,b):
    def home(self):
        super().home()
        print("home from child")
# obj=a()
# obj.home()
obj = c()
obj.home()
 