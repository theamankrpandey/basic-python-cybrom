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


# palindrome number
# n=int(input("enter a number to check is palindrome or not"))
# o=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if o==rev:
#     print("palindrome")
# else:
#     print("not palindrome")


# Armstrong Number
# n=int(input("enter a number"))
# count=0
# arm=0
# o=n
# while n>0:
#     n=n//10
#     count+=1
# while n>0:
#     digit=n%10
#     arm=arm+digit**count
#     n=n//10
# if o==arm:
#     print("arm")
# else:
#     print("not")


# print factor of numbers
# n=int(input("enter a number to find the factor"))
# for i in range(1,(n//2)+1):
#     if n%i==0:
#         print(i)
# print(n)

# optimal solution of factor of numbers
# from math import sqrt
# l=[]
# n=int(input("emter a number"))
# for i in range(1,int(sqrt(n))+1):
#     if n%i==0:
#         l.append(i)
#         if n//i!=i:
#             l.append(n//i)
# print(l)


# store the factor of number in a list form
# n=int(input("enter a number to find the factor"))
# li=[]
# for i in range(1,n+1):
#     if n%i==0:
#         li.append(i)
# print(li)

#  move zero in the end of the list using function
def hello(l):
    if len(l)==0:
        return
    i=0
    while i<len(l):
        if l[i]==0:
            break
        i+=1
    if i==len(l):
        return
    j=i+1
    while j<len(l):
        if l[j]!=0:
            l[i],l[j]=l[j],l[i]
            i+=1
        j+=1
l=[1,2,0,5,0,1,0]
hello(l)
print(l)