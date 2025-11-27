# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()'''

# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

# 1
# 2 3
# 4 5 6
# 7 8 9 10
'''n=int(input("enter a number"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()'''  

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*2,end=" ")
    print()'''

# 2
# 4 6
# 8 10 12
# 14 16 18 20
# 22 24 26 28
''''n=int(input("enter a number"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num*2,end=" ")
        num+=1
    print()'''

         # 1
        #1  2
      #1  2  3
    #1  2  3  4
  #1  2  3  4  5
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 

     # 2
    #2  4
  #2  4  6
 #2  4  6  8
#2 4  6  8 10

'''n=int(input("enter a number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j*2,end=" ")
    print()'''


# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=" ")
    print()'''


# A
# A B
# A B C
# A B C D
# A B C D E
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()'''

# A
# B C
# D E F
# G H I J
# K L M N O
'''n=int(input("enter a number"))
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()'''


# A
# A C
# A C E
# A C E G
# A C E G I
'''n = int(input("enter a number: "))
for i in range(1, n + 1):
    ch = 65 
    for j in range(1, i + 1):
        print(chr(ch), end=" ")
        ch += 2   
    print()'''

         #A
       # A B
     #  A B C
    # A  B C D
  # A  B  C  D E
'''n=int(input("enter a number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()'''

# A
# B C
# D E F
# G H I J
# K L M N O

'''n=int(input("enter a number"))
for i in range(1,n+1):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()'''

# A
# A C
# A C E
# A C E G
# A C E G I
'''n=int(input("enter a number"))
for i in range(1,n+1):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=2
    print()'''  


# *
# * *
# * * *
# * * * *
# * * * * *
'''n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''



        # *
      # * *
    # * * *
  # * * * *
# * * * * *
'''n=int(input("enter a number"))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''  

      # *
     # * *
    # * * *
   # * * * *
  # * * * * *
'''n=int(input("enter a number"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

# * * * * *
# * * * *
# * * *
# * *
# *
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

  # * * * * *
    # * * * *
      # * * *
        # * *
          # *
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''



    # * * * * *
     # * * * *
     # * * *
     # * *
      # * 
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''


    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
'''n=int(input("enter a number"))
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''


# Q.3(a)Write a  program to print the following pattern
# Sample :
# A B C D E
# F G H I
# J K  L
# M N
# O

# n=int(input("enter a number"))
# ch=65
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()


# Write a program to count occurrences of all characters within a string
# Sample :
# Input: “apple”
# Output:a-1,p-2,l-1,e-1
# n=input("Enter a string : ")
# ch={}
# for i in n:
#     if i not in ch:
#         ch[i] = 1
#     else:
#         ch[i] += 1

# for j in ch:
#     print(j, "-", ch[j])


# Q.4(a)Count and print how many times 'football' appears in list.
# Sports=[‘cricket’,’football’,’tennis’,’football’,’hockey’]

    
