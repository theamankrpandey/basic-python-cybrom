# def hello():
#     print("hello world")
# hello()



# function
# def display():
#     print("hello world")
# print(display())

# output
# hello world
# None




# def display():
#     print("hello")
# x=display()


# def display():
#     return"hello"
# print(display())


# def display():
#     return"hello"
# x=display()
# print(x)
# print(x)
# print(x)

# def display ():
#     print("hello")
# print("hii.....")
# print("welcome.....")
# x=display()
# print(display())

#average of three numbers
# def avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
# avg(1,2,3)  


# wap to find the factorial of n.(n is the parameter)
# def fact(n):
#     faco=1
#     for i in range(1,n+1):
#         faco=faco*i
#     print("fact is ",faco)
# fact(5)


# def fun_name(x,y,z,end=","):
#     print(f'the value of total arguments{x,y,z}')
# p=int(input("enter any value"))
# q=int(input("enter any value"))
# # r=int(input("enter any value"))
# fun_name(p,q)

# default argument
# def fun_name(x=0,y=0,z=0):
#     print(f'{x,y,z}')
# fun_name()

# def fun_name(**aman):
#     print(aman)
#     print(type(aman))
# t=eval(input("enter"))
# fun_name(**t)

# def add_all(*n):
#     sum=0
#     for i in n:
#         sum+=i
#     print(f'sum is {sum}')
# add_all(10,20,30,40,50)


# def add_all(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum+=j
#         print(f'sum is {sum}')
# t=eval(input("enter a tuple"))
# add_all(t)


# for unpacking the variable for code readunce
# def add_all(*n):
#     sum=0
#     print(n)
#     for i in n:
#         sum+=i
#     print(f'sum is {sum}')
# t=eval(input("enter a tuple"))
# add_all(*t)

# def fun_name(x,y,z):
#     print(f'{x,y,z}')
# fun_name(z=10,y=20,x=30)

# def display(x=0,y=0):
#     print(f'{x,y}')
# display(10,20)


# def display(x,y=0,*z):
#     print(x,y,z)
# display(10,20,30,40,50)


# def display(x,z,*n):
#     print(x ,n,z)
# display(10,20,30)

# def fun_name(**kwargs):
#     print(kwargs)
# t=eval(input("enter"))
# fun_name(**t)


# def fun_name(**n):
#     for k,w in n.items():
#         print(f'{k}={w}')
# t=eval(input("enter"))
# fun_name(**t)

# def display(p,q,r=0,*s):
#     print(p,q,r,s)
# display(10,20,30,40,50)


# with arguments and with return
# def show_detail(n):
#     return n
# x=input("enter your name")
# result=show_detail(x)
# print(result)


# with arguments and without return
# def show_detail(n):
#     print(n)
# x=input("enter your name")
# show_detail(x)

# without  arguments and without return
# def show_detail():
#     print("hello")
    # using walrus operator
#     print(a:="hii")
# show_detail()


# without argument and with return
# def show_detail():
#     return "hello"
# print(show_detail())
# show_detail()

# return type with argument
# def show(a,b):
#     return a+b
# data=show(5,6)
# print(show(5,6))


# non-return type with argument
# def hello(a,b):
#     print(a*b)
# hello(5,6)

#armstrong  number
# def armstrong(num):
#     power=len(str(num))
#     arm=0
#     o=num
#     i=1
#     while num>0:
#         digit=num%10
#         arm=arm+digit**power
#         num=num//10
#     if (o==arm):
#         print("armstrong number")
#     else:
#         print("not armstrong")
# n=int(input("enter a number"))
# armstrong(n)

#frequency in list
# def fre(n):
#     l={}
#     for i in n:
#         l[i]=l.get(i,0)+1
#     print(l)
# n=list(input("enter a number"))
# fre(n)

# reverse
# def hello

# waf to print 0th number end of the list
# def hello(n):
#     if len(n)==1:
#         return
#     i=0
#     while i<len(n):
#         if n[i]==0:
#             break
#         i+=1
#         if i==len(n):
#             return
#         j=i+1
#         while j<len(n):
#             if n[j]!=0:
#                 n[i],n[j]=n[j],n[i]
#                 i+=1
#             j+=1
# n=list(map(int,input("enter a number with space").split()))
# hello(n)
# print(n)


