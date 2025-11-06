# def hello():
#     for i in range(500):
#         yield i
# res=hello()
# print(res)
# # print(next(res))
# # print(next(res))
# for j in res:
#     print(j+1)


def data():
    for i in range(1,10):
        yield i
x=data()
for i in x:
    print(i+1)         
# print(next(x))
# for i in x:
    # print(i)