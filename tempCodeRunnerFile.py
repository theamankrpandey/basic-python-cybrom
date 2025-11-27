class hello:
        def __iter__(self):
                self.num=1
                return self
        def __next__(self):
                x=self.num
                self.num+=1
                return x
obj=hello()
myiter = iter(obj)
print(next(myiter))