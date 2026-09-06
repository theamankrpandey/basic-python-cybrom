# l=[5,7,3,2,6,1,5,9]
# def hello(nums,s,stop):
#     if s>=stop:
#         return
#     nums[s],nums[stop]=nums[stop],nums[s]
#     hello(nums,s+1,stop-1)
# hello(l,0,len(l)-1)
# print(l)



# a = [1,2,3,4]
# b=[]
# for i in a:
#     b=[i]+b
# print(b)

 
name='aman'
rev=''
new=''
for n in range(len(name)):
        rev=name[n]+rev
print(rev)
for i in range(len(rev)):
    if i==1:
        new+="b"
    else:
         new=new+rev[i]
print(new)
           
