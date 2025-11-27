# reverse a list using funtion
# def rev(a):
#     return a[::-1]

# num = int(input("Enter number of data "))
# data=list()
# for i in range(1,num+1):
#     data.append(int(input(f"Enter{i}  Number ")))
# print(rev(data))

# move zero in the end of the list using function
# perfect number using funtion



# Q.2(b)Write a program to count occurrences of all characters within a string
# Sample :
# Input: “apple”
# Output:a-1,p-2,l-1,e-1

# n=input("enter a string")
# ch={}
# for i in n: 
#     if i not in ch:
#         ch[i]=1
#     else:
#         ch[i]+=1
# for j in ch:
#     print(j,"-",ch[j],",",end="")




# Q.4(a)Count and print how many times 'football' appears in list.
# Sports=[‘cricket’,’football’,’tennis’,’football’,’hockey’]

# n = input("enter a list with space: ").split()
# sports=["cricket","football","tennis","football","hockey"]
# count=0
# for i in sports:
#     if i=="football":
#         count+=1
# print(f'{'football'}-{count}')




# Q.4(b)Find and print the largest and smallest number in a list [8, 2, 15, 1, 9] without using max() and min().

# n=list(map(int,input("enter a number to find smallest number").split()))
# l=len(n)
# for i in range(0,l):
#     for j in range(i+1,l):
#         if n[j]<n[i]:
#             n[j],n[i]=n[i],n[j]
# print(n[0])

# n=list(map(int,input("enter a number greatest").split()))
# l=len(n)
# for i in range(0,l):
#     for j in range(i+1,l):
#         if n[j]>n[i]:
#             n[j],n[i]=n[i],n[j]
# print(n[0])
# print(n)

# Use a lambda with the map() function to double each element in a list
# Input:[2,4,6,8]
# Output:Number of object-[4,8,12,16]

# n=list(map(int,input("enter a number").split()))
# print(list(map(lambda i:i*2,n)))


# Q.8(b) Write a python class  to reverse string word by word.
# Input:”All The Best”
# Output: “Best The All”

# n=input("enter a string")
# l=n.split()
# rev=l[::-1]
# print(" ".join(rev))


# Q.9(a) Use a lambda with the sorted() function to sort a list of tuples based on the second element
 
# Input:data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
# Output:data=[(‘date’,1),(‘banana’,2),(‘apple’,5),(‘cherry’,8)]
 
# data =  [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
# print(sorted(data,key=lambda x:x[1]))


# Q.9(b) Write a Python program to create a person class. Include attributes like name, 
# country and date of birth. Implement a method to determine the person's age.
# Output:Person:1
#              Name:Rahul Verma
#             Country:India
#             DOB:16/09/2000
#             Age:25

# from datetime import date
# class person:
#     def __init__(self,name,country,DOB,Age):
#         self.n=name
#         print(f'Name:{self.n}')
#         self.c=country
#         print(f'Country:{self.c}')
#         self.d = date()
#         print(f'DOB:{self.d}')
#         self.a=Age
#         today=date.today()
#         age=today.year-DOB.year
#         age = today.year - DOB.year 
#         ((today.month, today.day) <
#         (DOB.month, DOB.day))
#         print(age)
#         print(f'Age:{self.a}')
# d=person("Rahul","India","16/9/2000",25)    

# count dublicte from a set
# s=[1,2,1,2,1]
# a={}
# for i in s:
#     if i not in a:
#         a[i]=0
#     else:
#         a[i]+=1
# for j in a:
#     print(j,"-",a[j])


# Q.10(a) Create an Abstract base class called Vehicle with 
# two abstract methods start_engine() and Get_fuel_type()
#  that all vehicle types must implement,plus a concrete method 
# get_info() that provides common vehicle information.

# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     def __init__(self,name,color):
#         self.n=name
#         self.c=color
#     @abstractmethod
#     def start_engine(car):
#         pass
#     @abstractmethod
#     def get_fuel(car):
#         pass
#     def get_info(self):
#         print(self.n)
#         print(self.c)
# class car(vehicle):
#     def start_engine(vehicle):
#         print("The car engine is started")
#     def get_fuel(vehicle):
#         print("This car is petrol type")
#     def get_info(self):
#         print(self.n)
#         print(self.c)   
# d=car("mastang","pink")
# d.get_info()
# d.start_engine()
# d.get_fuel()



# Q.10(b) Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.)






# Q.6(b) Write a python class to implement pow(b,p) without using inbuilt function. Or operator.
# Input:pow(2,3)
# Output:8

# class p:
#     def power(self,a,b):
#         result=1
#         while b>0:
#             result=a*result
#             b=b-1
#         return result
# d=p()
# print(d.power(2,3))