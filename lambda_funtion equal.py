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

# age=lambda age:"eligible" if age>=18 else "not eligible"
# print(age(79))

# Write a lambda function to add two numbers.
# a=lambda x,y:x+y
# print(a(3,5))

# Write a lambda function to find the square of a number.
# a=lambda x:x*x
# print(a(5))

# Write a lambda function to find the maximum of two numbers.
# a= lambda x,y:x if x>y else y
# print(a(5,6))

# Write a lambda function to check if a number is even or odd.
# x= lambda a:"even" if a%2==0 else "odd"
# print(x(7))

# Write a lambda function to get the length of a given string.
# a= lambda a:len(a)
# print(a("hello"))

# Write a lambda function to reverse a string.
# a=lambda x:x[::-1]
# print(a("hello"))

# Write a lambda function to check if a string is a palindrome.
# x=lambda a:"palindrome" if a[::-1]==a else "not"
# print(x("aman"))



# Write a lambda function to find the cube of a number.
# x= lambda a:a**3
# print(x(2))

# Write a lambda function to find the largest number in a list using max() and key=lambda.
# x=lambda a:max(a)
# print(x([1,2,4]))

# Write a lambda function to sort a list of tuples based on the second element.
# x=lambda a:sorted(a,key=lambda a:a[1])
# print(x([(1, 3), (4, 2), (5, 1)]))
