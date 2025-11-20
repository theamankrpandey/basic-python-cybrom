# map() - return multiple data
# data=[1,3,4,5,6]
# ans = list(map(lambda x:x*x,data))
# print(ans)
# filter() - data which satisfy the conditions or only true
# data=[1,3,4,5,6,20]
# ans = list(filter(lambda x:x>=18,data))
# print(ans)
# reduce() - returns only single data
# from functools import reduce
# data=[1,3,4,5,6,20]
# ans = reduce(lambda x,y:x+y,data)
# print(ans)
# syntex - (funtion,iterable-object)


# 1) Square each number in a list using map()
# l=[1,2,3,4]
# x=list(map(lambda x:x*x,l))
# print(x)

# 2) Convert all strings in a list to uppercase using map()
# l=["aman"]
# p=list(map(str.upper,l))
# print(p)

# 3) Add 10 to each number using map()**
# l=[5,10,15]
# print(list(map(lambda x:x+10,l)))

# 4) Filter out even numbers using filter()**
# l=[2,3,4,5,6]
# print(list(filter(lambda x:x if x%2==0 else None,l)))

# 5) Filter strings starting with 'A'
# l="Aman","Anish","anuj","Deepak","Shravan"
# print(list(filter(lambda x:x if x[0]=="A" else None,l)))

# 6) Sum of numbers using reduce()
# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:x+y,l))x

# 7) Product of numbers using reduce()
# from functools import reduce
# l=[2,3,4]
# print(reduce(lambda x,y:x*y,l))

# 8) Filter words with length > 5
# l="aman","ujjwal","deepak","shravan"
# p=list(filter(lambda x:x if len(x)>5 else None,l))
# print(p)

# Convert integers to strings using map()
# a=[1,2,4,4,5]
# a=list(map(lambda x:str(x) ,a))
# print(a)

# 10) Find maximum using reduce()
# from functools import reduce
# n = [1,2,3,4,5]
# a=reduce(lambda x,y:y if x>y else y,n)
# print(a)    

# 11) Squares only of even numbers using map()
# x=[1,2,3,4,5]
# print(list(map(lambda x:x*x ,filter(lambda x: x%2==0 ,x))))

# 2) Filter palindromes using filter()