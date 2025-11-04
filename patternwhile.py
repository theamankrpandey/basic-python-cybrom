# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print('*'*n)
#     i+=1

# print like this
# *
# **
# ***
# ****
# *****
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print('*'*i+''*(n-i))
#     i+=1


# print like this
#     *
#    **
#   ***
#  ****
# *****
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1


# print like this
#     *     
#    * *    
#   * * *   
#  * * * *  
# * * * * * 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1


# inverted pyramid
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# n=int(input("enter a number"))
# i=0
# while i<=n:
#     print(" "*i+"* "*(n-i))
#     i+=1


# print like this
# ****
# ***
# **
# *
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print('*'*(n-i))
#     i+=1


# print like this
# *****
#  ****
#   ***
#    **
#     *
# n=int(input("enter a number"))
# i=0
# while i<=n:
#     print(" "*i+'*'*(n-i))
#     i+=1



# print like this
# *    
# **   
# ***  
# **** 
# *****
# *****
# **** 
# ***  
# **   
# *    
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print("*"*i+" "*(n-i))
#     i+=1
# i=0
# while i<=5:
#     print("*"*(n-i)+" "*i)
#     i+=1




# print like this pattern
# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****
# n=int(input("enter a number"))
# i=0
# while i<n:
#     print("*"*(n-i))
#     i+=1
# i=1
# while i<=n:
#     print("*"*i)
#     i+=1



# print like this
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# n=int(input("enter a number"))
# i=0
# while i<=n:
#     print(" "*(n-i)+"* "*i)
#     i+=1
# i=1
# while i<=n:
#     print(" "*i+"* "*(n-i))
#     i+=1


# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# n=int(input("enter a number"))
# i=0
# while i<=n:
#     print(" "*i+"* "*(n-i))
#     i+=1
# i=1
# while i<=n:
#     print(" "*(n-i)+"* "*i)
#     i+=1



# print like this
# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     ch="a"
#     j=1
#     while j<=n:
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#         j+=1
#     print()
#     i+=1





# a 
# a b 
# a b c 
# a b c d 
# a b c d e 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     ch='a'
#     j=1
#     while j<=i:
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#         j+=1
#     print()
#     i+=1




#     a 
#    a b 
#   a b c 
#  a b c d 
# a b c d e 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     print(" "*(n-i),end="")
#     ch='a'
#     j=1
#     while j<=i:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#         j+=1
#     print()
#     i+=1




# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# n=int(input("enter a number"))
# i=1
# num=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(num,end=' ')
#         num+=1
#         j+=1
#     print()
#     i+=1



1 
# 1 3 
# 1 3 5 
# 1 3 5 7 
# 1 3 5 7 9 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     num=1
#     j=1
#     while j<=i:
#         print(num,end=' ')
#         num+=2
#         j+=1
#     print()
#     i+=1


# 2 
# 2 4 
# 2 4 6 
# 2 4 6 8 
# 2 4 6 8 10
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     j=1
#     num=2
#     while j<=i:
#         print(num,end=" ")
#         num+=2
#         j+=1
#     print()
#     i+=1