# interview question
f=open('n1.txt','a+')
# print(f.tell())
print(f.seek(0))
data = f.read()
print(data)