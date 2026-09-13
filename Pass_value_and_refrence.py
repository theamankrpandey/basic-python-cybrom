def change(x): #parameter
    print(x)
    
change(x= 10)  # argument


'''
Pass by Value: Function ko variable ki copy milti hai. Function ke andar value change karo to original variable pe koi asar nahi padta.
Pass by Reference: Function ko variable ka actual memory address (reference) milta hai. Function ke andar change karo to original bhi change ho jata hai.
'''


'''Pass By Value'''
a=10
b=a
b=20
print(a)
print(b)

'''Pass By Reference'''
a=[10]
b=a
b=20
print(int(a[0])) # Typecasting
print(b)