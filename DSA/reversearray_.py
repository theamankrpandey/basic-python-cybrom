l=[5,7,3,2,6,1,5,9]
def hello(nums,s,stop):
    if s>=stop:
        return
    nums[s],nums[stop]=nums[stop],nums[s]
    hello(nums,s+1,stop-1)
hello(l,0,len(l)-1)
print(l)