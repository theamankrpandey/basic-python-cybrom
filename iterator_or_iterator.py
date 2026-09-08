# l=[1,2,3,4,5,'python']
# l1=iter(l)
# print(next(l1))
# print(next(l1))
# print(next(l1))

'''Iteration ka simple meaning hai: kisi collection ke elements ko ek-ek karke access karna'''
a = [10, 20, 30, 40]
for x in a:
    print(x)
    print(f"{x} execute")



'''Iterator ek object hota hai jo elements ko ek-ek karke return karta hai.'''
a = [10, 20, 30, 40]
it = iter(a)
print(next(it))




