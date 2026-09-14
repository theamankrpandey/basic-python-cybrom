# class A:
#   def One(self):
#     print("A")

# class B(A):
#   def One(self):
#     super().One()
#     print("B")
# class C(B,A):
#   def Two(self):
#     print("C")

# c=C()
# c.One()
      
      

    
'''reverse list'''
l=[1,2,3,4]
j=len(l)-1
for i in range(len(l)):
  if i<j:
    l[i],l[j]=l[j],l[i]
    j=j-1
print(l)



'''frequency count'''
# s="hello"
# a={}
# for i in range(len(s)):
#   if s[i] not in a:
#     a[s[i]]=1
#   else:
#     a[s[i]]+=1
# print(a)




# '''Remove Dublicate'''

# a=[1,2,3,3,4,5,5,6,7,7]
# s=[]
# for i in range(len(a)):
#   if a[i] not in s:
#     s=s+[a[i]]
# print(s)



'''Dice have 6 number six times '''



# def add():
#   for i in range(7):
#     yield i
# a=add()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# import random
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))


# l=[1,2,3,4,5,6]
# print(random.choice(l))
# print(random.choice(l))
# print(random.choice(l))
# print(random.choice(l))
# print(random.choice(l))
# print(random.choice(l))




'''second largest element'''
# l=[1,2,114,5,4,67]
# largest=0
# Second_largest=0
# for i in l:
#   if i>largest:
#     Second_largest = largest
#     largest = i
#   elif i<Second_largest:
#     Second_largest=i
# print(Second_largest)    
    
    
'''important'''
# li = [9,9]

# for i in range(len(li)-1,-1,-1):
#   if li[i] != 9:
#     li[i]+=1
#     break

#   if li[i] == 9:
#     li[i]=0

# if(li[0] == 0):
#   li.insert(0,1)
    
# print(li)


'''Amagram'''
# a="hello"
# b="olleh"
# c={}
# d={}
# for i in range(len(a)):
#   if a[i] not in c:
#     c[a[i]]=1
#   else:
#     c[a[i]]+=1
# for j in range(len(b)):
#   if b[j] not in d:
#     d[b[j]]=1
#   else:
#     d[b[j]]+=1
# if c==d:
#   print("Anagram")
# else:
#   print("Not Anagram")

    
      