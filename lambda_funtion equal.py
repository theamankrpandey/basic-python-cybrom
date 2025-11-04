# p=lambda x,y:print(x+y)
# z=p(4,5)
# print(z)

# l=[1,2,3,4,5]
# print(list(map(lambda n:n*n,l)))



# l1=[1,2,3,4,5]
# l2=[2,3,4,5,5]
# l3=[2,3,4,5,6]
# print(list(map(lambda x,y,z:x*y*z,l1,l2,l3)))


# l=[1,2,3,4,5,6,7,8]
# print(list(filter (lambda n:n if n%2==0 else'odd',l)))

# l=[1,2,3,4,5,6,7,8]
# print(list(map (lambda n:n if n%2==0 else'odd',l)))

# import functools 
# l=[1,2,3,4,5,6,7,8]
# print(functools.reduce(lambda x,y :x+y,l))

# import functools 
# l=[1,2,3,4,5,6,7,8]
# print(functools.reduce(lambda x,y:x if x>y else y,l))
# print(functools.reduce(lambda x,y:x if x<y else y,l))