l=[5,7,3,2,6,1,5,9]
def hello(nums,s,stop):
    if s>=stop:
        return
    nums[s],nums[stop]=nums[stop],nums[s]
    hello(nums,s+1,stop-1)
hello(l,0,len(l)-1)
print(l)

name='aman'
rev=''
for i in range(len(name)-1,-1,-1):
    rev+=name[i]


l=[5,7,3,2,6,1,5,9]
rev=[]
for  element in l:
    rev=[element]+rev
print (rev)

 
name='aman'
rev=''
for n in name:
    rev='n'+rev
print(rev)