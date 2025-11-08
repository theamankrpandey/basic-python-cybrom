# Question 1. Write a program to convert a list of tuples into a dictionary.
# Example Input: [(1, &#39;a&#39;), (2, &#39;b&#39;), (3, &#39;c&#39;)]

# n=[(1, 'a'), (2, 'b'), (3, 'c')]
# print(dict(n))


# Write a Python program to print a hollow pyramid pattern. The program 
# should ask for a single integer input, n, which represents the height of the pyramid?
#     *
#    * *
#   *   *
#  *     *
# *********

# n=int(input("enter a number to print a pattern"))
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i==n or i+j==n+1 or j-i==n-1:
#             print("*",end="")
#         else:
#             print(' ',end="")
#     print()


# Write a python program to create the logic of sorting into ascending order
# n=[3,4,5,6,7,1]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]>n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)



#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA


# n=int(input("enter a number"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# reverse a number
# n=int(input("enter a number"))
# def hello(n):
#     count=0
#     while n>0:
#        count+=1
#        n=n//10
#     return count
# hello(n)


# count a digit
# n=int(input("enter a number"))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)



# n=int(input("enter a number"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)