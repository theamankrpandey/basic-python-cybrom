# operator,funtion method which changes its output depending on its data type
# class student:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
# data=student()
# data.add(5,6)


# st = "pythonprogramming"
# print(len(st))
# li = [1,3,4,4,1]
# print(len(li))
# li = (1,3,4,4,1)
# print(len(li))



class calculator:
    def Calculation(self,num1=0,num2=0):
        if(num1!=0 and num2!=0):
            print(num1*num2)
        if(num2==0):
            print(num1+num2)
        if(num1==0 and num2==0):
            print(0)

obj = calculator()
obj.Calculation(4)
obj.Calculation()
obj.Calculation(5,77)