# a=['x','y','z',1,2,3]
# d1=dict.fromkeys(a,5)
# print(d1)

# d1={'x':10,'y':20,'z':30}
# d2={'p':10,'q':20,'x':30}
# a=d1.update(d2)
# print(d1)


# d1={'x':10,'y':20,'z':30}
# d=d1.setdefault('x',"aman")
# print(d)

# a=[1,2,3,'a','b','c']
# d1=dict.fromkeys(a,5)
# print(d1)

# a={1:10,2:20,3:30}
# print(tuple(a.keys()))  
# print(a)

# d={1:'a',2:'b',3:'c'}
# print(d.popitem())
# d1={4:'b'}
# d.update(d1)
# print(d.items()) 


# d={1:'a',2:'b',3:'c'}
# d1=d.copy()
# print(id(d))
# print(id(d1))
# d.clear()
# print(d)
# print(id(d))
# del d
# print(d)

'''dindur method 
print(dir(dict))'''


# wap to enter marks of 3 subjects from the user and store them
#  in a dictionary.start with an empty dictionary & add one by one.
# use subjects name as key & marks as value
# dict={}
# a=eval(input("enter your first marks"))
# dict.update({"che":a})
# b=eval(input("enter your second marks"))
# dict.update({"eng":b})
# c=eval(input("enter your third marks"))
# dict.update({"hindi":c})
# print(dict)