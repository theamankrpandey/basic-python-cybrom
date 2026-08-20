class student:
    school="jnv" #instance variable
    def __init__(self,name):
        self.name=name #local variable
    def display(self):
        message="welcome"
        print(message)
s1=student("am")
s1.display()
print(s1.school)



# class student:
#     school="jnv" #instance variable
#     def __init__(self):
#         pass
#          #local variable
#     def display(self):
#         message="welcome"
#         print(message)
# s1=student()
# s1.display()
# print(s1.school)


class student:
    school="jnv" #static variable or class varible in the code we defining the how to acces 
    def __init__(self,name):
        student.name=name
    def display(self):
        student.graduate="b.tech"
s1=student("aman")
print(s1.name)
print(s1.school)
s1.display()
print(s1.graduate)