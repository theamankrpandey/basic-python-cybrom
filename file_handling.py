# interview question
# f=open('n1.txt','a+')
# # print(f.tell())
# print(f.seek(0))
# data = f.read()
# print(data)


# with open("n1.txt", "rb") as f:
#     # data = f.write("hello\nthis is aman")
#     print(f.tell())
#     a=f.seek(5)
#     print(a)
#     b=f.seek(0,2)
#     b=f.seek(-5,1)
#     b=f.seek(5,1)
#     print(b)



with open("n1.txt", "rb") as f:
    # data = f.write("hello\nthis is aman")
    print(f.tell())
    # print(f.read(7))
    # print(f.tell())
    print(f.seek(1,1))
    print(f.seek(0,2))
    print(f.seek(-5,2))
    print(f.read())
    
    # print(f.seek(-5,1))
    # print(f.tell())