class A:
  def One(self):
    print("A")

class B(A):
  def One(self):
    super().One()
    print("B")
class C(B,A):
  def Two(self):
    print("C")

c=C()
c.One()
      
      

    
'''reverse list'''
l=[1,2,3,4]
j=len(l)-1
for i in range(len(l)):
  if i<j:
    l[i],l[j]=l[j],l[i]
    j=j-1
print(l)




s="hello"
a={}
for i in range(len(s)):
  if s[i] not in a:
    a[s[i]]=1
  else:
    a[s[i]]+=1
print(a)




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
'''second largest element'''
l=[3,2,114,5,74,67]
largest=0
Second_largest=0
for i in l:
  if i > Second_largest and i<largest:
    Second_largest=i

  if i>largest:
    largest=i
print(Second_largest)
print(largest)
    
    
    
    