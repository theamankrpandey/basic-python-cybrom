'''Q.1(a) Write a Python program to change a given string to a newly string
where the first and last chars have been exchanged.
Example:
Input:”welcome”
Output:”eelcomw”'''
# n=input("enter a string")
# l=list(n)
# l[0],l[-1]=l[-1],l[0]
# n="".join(l)
# print(n)

'''Q.2(b) Write a Python program to count the occurrences of each word in a
given sentence.
Example:
Input:”welcome to cybrom”
Output:3'''
# n=input("eneter a string")
# print(len(n.split()))

# without use split
# n=input("enter a string")
# count=1
# for i in n:
#     if i==" ":
#         count+=1
# print(count)


# n=list(input("enter a list"))
# a=str(n)
# print(len(a))



# input:-"python" output:- "qzuipo"
# n=input("enter a number")
# for i in n:
#     ch=chr(ord(i)+1)
#     print(ch,end=" ")
# print()

# Q.2(a) Write a Python program to check the given number is prime or not.
# n=int(input("enter a number"))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not")


# Q.2(b) Write a Python program to print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# Q.3(a) Write a Python program to get the smallest number from a list.
# Example:
# Input:[4,5,6,1,8]
# Output:1

l = list(map(int, input("Enter list items: ").split()))
small=l[0] 
for i in l:
    if i<small:
        small=i 
print(small)