s = "Aman Pandey"
a=""
for i in s:
    a=i+a
    # print(a)
print(a)

'''pandey Aman'''
a="Aman Pandey"
b=""
c=""
d=0
for i in a:
    if i == " ":
        d=1
        continue
    if d==0:
        b=b+i
    else:
        c=c+i
print(c+b)