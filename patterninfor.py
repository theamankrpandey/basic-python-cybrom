# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# n=int(input("enter a number"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#     *
#    **
#   ***
#  ****
# *****
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
# print()


#     *
#    ***
#   *****
#  *******
# *********
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()



# n = int(input("Enter the character range : "))
# for i in range(1,n+1):
#     print(' '*(n-i),end = '')
#     if i==1:
#         print('*')
#     elif i>1 and i!=n:
#         print('*' + ' ' * (i-1), end = '')
#         if i>2:
#             print(' ' * (i-2) + '*')
#         else:
#             print('*')
#     else:
#         print('*' * n + '*' * (n-1))
#    *   
#   * *  
#  *   * 
# *******



n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if i==4 or i+j==5 or j-i==3:
            print("*",end="")
        else:
            print(end=" ")
    print()

#    *   
#   * *  
#  *   * 
# *******