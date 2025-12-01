# n=int(input("enter a number"))
# ft=0
# st=1
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         next=ft+st
#         print(ft,end=" ")
#         next=ft
#         ft=st
#         st=next+ft
#         j+=1
#     print()
#     i+=1

# s=eval(input("enter "))
# for i in s.values:
#     print(i)
# print("thanks")


# n=int(input("enter a number"))
# ft=0
# st=1
# i=1
# while i<=n:
#     next=ft+st
#     print(ft,end=" ")
#     ft=st
#     st=next
#     i+=1


# while (True):
#     print("1.addition\n 2.substraction\n 3.multiply\n 4.division\n 5.exit")
#     n=int(input("enter any option"))
#     if n in (1,2,3,4,5):
#         if n in (1,2,3,4):
#             if n==1:
#                 sum,l=0,[]
#                 n=int(input("enter how many number do you want to add"))
#                 for i in range(1,n+1):
#                     value=(int(input(f'enter a number{i}value:')))
#                     l.append(value)
#                     sum=sum+value
#                 print(f'sum of given value is{l}is{sum}')
#             if n==2:
#                 sub,l=0,[]
#                 n=int(input("enter how many number substract"))
#                 for i in range(1,n+1):
#                     value=int(input(f'enter {i} number'))
#                     l.append(value)
#                     if i==1:
#                         sub=value
#                     else:
#                         sub=sub-value
#                 print(f'sub of given {l} is {sub}')
#     else:
#         print("choose a valid option")      


    
# *********
#  *******
#   *****
#    ***
#     *



#     n = 5
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2*i - 1))


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))  

# 1. Write a  program to find maximum between two numbers.
# a=10
# b=20
# if a>b:
#     print(a)
# else:
#     print(b)
