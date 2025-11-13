class student:
    college="rntu"
    def __init__(self,name,quali):
        self.n=name
        self.q=quali
    def detail(self):
        self.name=self.n
        self.college=student.college
data=student("aman","b.e")
print(data.n)
print(data.detail())