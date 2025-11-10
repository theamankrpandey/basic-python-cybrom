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
n=int(input("enter a number"))
count=0
arm=0
o=n
while n>0:
    n=n//10
    count+=1
while n>0:
    digit=n%10
    arm=arm+digit**count
    n=n//10
if o==arm:
    print("arm")
else:
    print("not")